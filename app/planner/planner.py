from app.llm.client import LLMClient


class Planner:

    def __init__(self):
        self.llm = LLMClient()

    def think(self, messages):
        return self.llm.chat(messages)
