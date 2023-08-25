import json

from dataset import Dataset
from model import Model

class Eval:
    def __init__(self, dataset: Dataset, model: Model) -> None:
        self.dataset = dataset
        self.model = model

    def run(self) -> None:
        self.model.set_key()
        for prompt in self.dataset.load():
            print(self.model.query(prompt))


if __name__ == "__main__":
    ds = Dataset("aqua", "data/dev.json")
    llm = Model("gpt-3.5-turbo")
    ev = Eval(ds, llm)
    ev.run()