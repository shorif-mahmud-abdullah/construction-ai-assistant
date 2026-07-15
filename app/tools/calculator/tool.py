from app.tools.base import Tool


class CalculatorTool(Tool):
    name = "calculator"

    description = (
        "Perform mathematical calculations. "
        "Input should be a valid mathematical expression."
    )
    usage = "Use when the user asks for a math calculation."
    example = 'User: What is 25 * 30?\nAssistant:\n{"tool": "calculator", "input": "25*30"}'
    def execute(self, expression: str):
        try:
            return str(eval(expression))
        except Exception:
            return "Invalid expression"
