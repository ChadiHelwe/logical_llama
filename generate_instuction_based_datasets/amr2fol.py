import os
from collections.abc import Generator
from typing import Tuple

from amr_logic_converter import AmrLogicConverter
from tqdm import tqdm


class AmrToFolConverter:
    def __init__(
        self, existentially_quantify_instances=True, capitalize_variables=False
    ):
        self.existentially_quantify_instances = existentially_quantify_instances
        self.capitalize_variables = capitalize_variables
        self.converter = AmrLogicConverter(
            existentially_quantify_instances=True, capitalize_variables=False
        )

    def convert(self, amr_input) -> str:
        """Convert the given AMR to FOL."""
        logic = self.converter.convert(amr_input)
        return str(logic)

    def extract_amr_and_sentences(self, file_path):
        """Extract the sentences and AMRs from the given file."""
        sentences = []
        amrs = []

        with open(file_path, "r") as f:
            amr = ""
            current_sentence = ""
            for line in f:
                if line.startswith("# ::snt"):
                    current_sentence = line.split("# ::snt")[1].strip()
                    continue
                elif line.startswith("#") or not line.strip():
                    if amr:
                        amrs.append(amr)
                        sentences.append(current_sentence)
                        amr = ""
                    continue
                amr += line

            if amr:
                amrs.append(amr)
                sentences.append(current_sentence)

        return sentences, amrs

    def process_directory(
        self, directory_path
    ) -> Generator[Tuple[str, str], None, None]:
        """Process all files in the given directory and yield the corresponding sentences and AMRs."""
        sentences = []
        amrs = []
        files = [
            os.path.join(directory_path, f)
            for f in os.listdir(directory_path)
            if f.endswith(".txt")
        ]

        for file_path in files:
            s, a = self.extract_amr_and_sentences(file_path)
            sentences.extend(s)
            amrs.extend(a)

        assert len(sentences) == len(amrs)
        print(f"Sentences: {len(sentences)}, AMRs: {len(amrs)}")

        error_count = 0
        for i, amr in enumerate(tqdm(amrs)):
            try:
                yield sentences[i], self.convert(amr)
            except Exception as e:
                error_count += 1

        print(len(sentences))
        print(f"Errors: {error_count} ({error_count / len(sentences) * 100:.2f} %)")


if __name__ == "__main__":
    converter = AmrToFolConverter()
    root_dir = "datasets/amr_annotation_3.0/data/amrs/unsplit/"
    for s, f in converter.process_directory(root_dir):
        print(s)
        print(f)
        print()
