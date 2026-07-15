from app.agent.agent import Agent


class Application:

    def __init__(self):
        self.agent = Agent()

    def run(self):
        print("=== Construction AI Assistant ===")
        while True:
            user_input = input("\nYou: ")
            if user_input.lower() in ["exit", "quit"]:
                break
            answer = self.agent.run(user_input)
            print(f"\nAssistant:\n{answer}")