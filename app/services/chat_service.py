from app.agent.agent import Agent


class ChatService:

    def __init__(self):
        self.agent = Agent()

    def chat(self, message: str):

        return self.agent.run(message)