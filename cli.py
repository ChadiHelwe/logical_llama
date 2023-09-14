
from src_logimancer.model import Logimancer


def train():
    model = Logimancer()
    model.train()    
    

def eval():
    model = Logimancer()

if __name__ == "__main__":
    import argparse 
    parser = argparse.ArgumentParser()
    parser.add_argument("train", help="train model", action="store_true")

    args = parser.parse_args()
    if args.train:
        train()
