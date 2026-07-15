from app.tools.calculator.tool import CalculatorTool
from app.tools.memory.tool import SaveNoteTool, ListNotesTool
from app.tools.construction.tool import RAGTool


class ToolRegistry:

    def __init__(self):
        self.tools = {
            "calculator": CalculatorTool(),
            "save_note": SaveNoteTool(),
            "list_notes": ListNotesTool(),
            "search_construction_docs": RAGTool(),
        }

    def get(self, tool_name: str):
        return self.tools.get(tool_name)

    def get_tool_descriptions(self):
        descriptions = []
        for tool in self.tools.values():
            descriptions.append(
                f"- {tool.name}: {tool.description} {tool.usage}\n  {tool.example}"
            )
        return "\n".join(descriptions)
