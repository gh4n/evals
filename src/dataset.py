import os
import json

from dataclasses import dataclass
from typing import Iterable


@dataclass
class Prompt:
    name: str
    question: str
    answer: str


class Dataset:
    def __init__(self, name: str, path: str) -> None:
        self.name = name
        self.path = path

    def load(self) -> Iterable[Prompt]:
        with open(self.path, "r") as f:
            text = f.readline()
            print(text)
            line = json.loads(text)
            prompt = Prompt(self.name, line["question"], line["correct"]) 
            yield prompt
