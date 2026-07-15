class PromptBuilder:

    def build(self, registry, conversation, user_input):
        tool_descriptions = registry.get_tool_descriptions()

        system_prompt = (
            "You are a helpful AI assistant for construction and engineering.\n"
            "You can also remember user information and do math.\n\n"
            "Available tools:\n"
            f"{tool_descriptions}\n\n"
            "Rules:\n"
            "- Use a tool ONLY when the user's request clearly matches one.\n"
            "- Use ONE tool per turn. Never call multiple tools at once.\n"
            "- If no tool is needed, answer directly without JSON.\n\n"
            "To use a tool, return ONLY valid JSON:\n"
            '{"tool": "...", "input": "..."}\n\n'
            "To answer without a tool, just reply normally."
        )

        messages = [{"role": "system", "content": system_prompt}]
        messages.extend(conversation.get_messages())
        messages.append({"role": "user", "content": user_input})

        return messages
