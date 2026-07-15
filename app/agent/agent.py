import json

from app.llm.client import LLMClient
from app.tools.registry import ToolRegistry
from app.memory.conversation import ConversationMemory
from app.planner.planner import Planner
from app.prompts.builder import PromptBuilder


class Agent:

    def __init__(self):
        self.planner = Planner()
        self.registry = ToolRegistry()
        self.memory = ConversationMemory()
        self.builder = PromptBuilder()

    def execute_tool(self, tool_name, tool_input):
        tool = self.registry.get(tool_name)
        if tool is None:
            return None
        return tool.execute(tool_input)

    def run(self, user_input: str):
        messages = self.builder.build(self.registry, self.memory, user_input)
        MAX_STEPS = 5
        final_answer = ""

        for _ in range(MAX_STEPS):
            response = self.planner.think(messages)

            try:
                tool_request = json.loads(response)
                tool_name = tool_request["tool"]
                tool_input = tool_request["input"]
                print(f"Tool requested: {tool_name}")

                result = self.execute_tool(tool_name, tool_input)
                if result is None:
                    final_answer = f"Unknown tool: {tool_name}"
                    break

                messages.append({"role": "assistant", "content": response})
                messages.append(
                    {
                        "role": "user",
                        "content": (
                            f"Tool result:\n{result}\n\n"
                            "Use this result to answer the user's question. "
                            "Reply directly — do NOT call another tool."
                        ),
                    }
                )
                continue

            except json.JSONDecodeError:
                final_answer = response
                break

        self.memory.add_user(user_input)
        self.memory.add_assistant(final_answer)
        return final_answer
