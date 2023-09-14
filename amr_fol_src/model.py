import os
import sys
import time
from pathlib import Path

import lightning as L
import numpy as np
import torch

# support running without installing as a package
wd = Path(__file__).parent.parent.resolve()
sys.path.append(str(wd))

from generate import generate
from lit_llama.lora import lora, lora_state_dict, mark_only_lora_as_trainable
from lit_llama.model import LLaMA, LLaMAConfig
from lit_llama.tokenizer import Tokenizer
from scripts.prepare_alpaca import generate_prompt


class Logimancer:
    def __init__(
        self,
        data_dir: str = "datasets",
        pretrained_path: str = "models/llama-2-7b/consolidated-00.pth",
        tokenizer_path: str = "models/llama-2-7b/tokenizer.model",
        out_dir: str = "out/lora/logicmancer",
        intruction_tuning=True,
        eval_interval=100,
        save_interval=100,
        eval_iters=100,
        log_interval=1,
        learning_rate=3e-4,
        batch_size=128,
        micro_batch_size=4,
        max_iters=5000000 * 3,
        weight_decay=0.0,
        max_seq_length=512,
        lora_r=8,
        lora_alpha=16,
        lora_dropout=0.05,
        warmup_iters=100,
    ):
        self.data_dir = data_dir
        self.pretrained_path = pretrained_path
        self.tokenizer_path = tokenizer_path
        self.out_dir = out_dir
        self.instruction_tuning = intruction_tuning
        self.eval_interval = eval_interval
        self.save_interval = save_interval
        self.eval_iters = eval_iters
        self.log_interval = log_interval
        self.learning_rate = learning_rate
        self.batch_size = batch_size
        self.micro_batch_size = micro_batch_size
        self.gradient_accumulation_iters = batch_size // micro_batch_size
        self.max_iters = max_iters // micro_batch_size
        self.weight_decay = weight_decay
        self.max_seq_length = max_seq_length
        self.lora_r = lora_r
        self.lora_alpha = lora_alpha
        self.lora_dropout = lora_dropout
        self.warmup_iters = warmup_iters
        self.model = None

    def __config(self, train=False):
        self.fabric = L.Fabric(accelerator="cuda", devices=1, precision="bf16-true")
        self.fabric.launch()
        self.fabric.seed_everything(1337 + self.fabric.global_rank)

        if self.fabric.global_rank == 0:
            os.makedirs(self.out_dir, exist_ok=True)

        config = LLaMAConfig.from_name("7B")
        config.block_size = self.max_seq_length

        checkpoint = torch.load(self.pretrained_path)

        with self.fabric.init_module(), lora(
            r=self.lora_r,
            alpha=self.lora_alpha,
            dropout=self.lora_dropout,
            enabled=True,
        ):
            self.model = LLaMA(config)
            self.model.load_state_dict(checkpoint["model"])

        self.tokenizer = Tokenizer(self.tokenizer_path)
        if train:
            self.train_data, self.val_data = self.__load_datasets(
                data_dir=self.data_dir
            )
            mark_only_lora_as_trainable(self.model)
            self.optimizer = torch.optim.AdamW(
                self.model.parameters(),
                lr=self.learning_rate,
                weight_decay=self.weight_decay,
            )

    def train(self):
        if self.model is None:
            self.__config(train=True)
        step_count = 0

        for iter_num in range(self.max_iters):
            if step_count <= self.warmup_iters:
                lr = self.learning_rate * step_count / self.warmup_iters
                for param_group in self.optimizer.param_groups:
                    param_group["lr"] = lr

            t0 = time.time()

            input_ids, targets = self.__get_batch(self.train_data)
            with self.fabric.no_backward_sync(
                self.model,
                enabled=((iter_num + 1) % self.gradient_accumulation_iters != 0),
            ):
                logits = self.model(input_ids=input_ids)
                loss = self.__loss_fn(logits, targets)
                self.fabric.backward(loss / self.gradient_accumulation_iters)

            if (iter_num + 1) % self.gradient_accumulation_iters == 0:
                self.optimizer.step()
                self.optimizer.zero_grad()
                step_count += 1

                if step_count % self.eval_interval == 0:
                    val_loss = self.__validate()
                    self.fabric.print(f"step {iter_num}: val loss {val_loss:.4f}")
                    self.fabric.barrier()

                if step_count % self.save_interval == 0:
                    print(f"Saving LoRA weights to {self.out_dir}")
                    checkpoint = lora_state_dict(self.model)
                    self.fabric.save(
                        os.path.join(self.out_dir, f"iter-{iter_num:06d}-ckpt.pth"),
                        checkpoint,
                    )

            dt = time.time() - t0
            if iter_num % self.log_interval == 0:
                self.fabric.print(
                    f"iter {iter_num}: loss {loss.item():.4f}, time: {dt*1000:.2f}ms"
                )

        self.checkpoint = lora_state_dict(self.model)
        self.fabric.save(
            os.path.join(self.out_dir, "lit-llama-lora-finetuned.pth"), checkpoint
        )

    def generate(self, instruction, input_text):
        if self.model is None:
            self.__config()

        self.model.eval()
        prompt = instruction
        sample = {"instruction": instruction, "input": input_text}
        if self.instruction_tuning:
            sample["instruction"] = generate_prompt(
                sample["instruction"], self.tokenizer
            )

        encoded = self.tokenizer.encode(
            prompt, bos=True, eos=False, device=self.model.device
        )

        output = generate(
            self.model,
            idx=encoded,
            max_seq_length=self.max_seq_length,
            max_new_tokens=100,
        )
        output = self.tokenizer.decode(output)
        return output  # output.split("### Response:")[1].strip()

    @torch.no_grad()
    def __validate(self):
        self.fabric.print("Validating ...")
        self.model.eval()
        losses = torch.zeros(self.eval_iters)
        for k in range(self.eval_iters):
            input_ids, targets = self.__get_batch(self.val_data)
            logits = self.model(input_ids=input_ids)
            loss = self.__loss_fn(logits, targets)
            losses[k] = loss.item()
        out = losses.mean()
        self.model.train()
        return out.item()

    def __load_datasets(self, data_dir):
        train_data = torch.load(os.path.join(data_dir, "train.pt"))
        val_data = torch.load(os.path.join(data_dir, "test.pt"))
        return train_data, val_data

    def __loss_fn(self, logits, targets):
        logits = logits[..., :-1, :].contiguous()
        targets = targets[..., 1:].contiguous()
        loss = torch.nn.functional.cross_entropy(
            logits.view(-1, logits.size(-1)), targets.view(-1), ignore_index=-1
        )
        return loss

    def __get_batch(self, data):
        ix = torch.randint(len(data), (self.micro_batch_size,))

        input_ids = [data[i]["input_ids"].type(torch.int64) for i in ix]
        labels = [data[i]["labels"].type(torch.int64) for i in ix]

        max_len = max(len(s) for s in input_ids)

        def pad_right(x, pad_id):
            # pad right based on the longest sequence
            n = max_len - len(x)
            return torch.cat((x, torch.full((n,), pad_id, dtype=x.dtype)))

        x = torch.stack([pad_right(x, pad_id=0) for x in input_ids])
        y = torch.stack([pad_right(x, pad_id=-1) for x in labels])

        x, y = self.fabric.to_device((x.pin_memory(), y.pin_memory()))
        return x, y
