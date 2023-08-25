import os

import openai

from dataset import Prompt


class Model:

    def __init__(self, name: str) -> None:
        self.name = name
        self.api_key = os.getenv("OPENAI_API_KEY")

    def set_key(self) -> None:
        openai.api_key = self.api_key
        
    def query(self, input: Prompt) -> str:
        print(openai.api_key)
        ans = openai.ChatCompletion.create(model=self.name, messages=[{"role": "user", "content": input.question}])
        return ans.choices[0].message.content

