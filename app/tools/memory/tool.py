from app.tools.base import Tool
from app.tools.memory.repository import NoteRepository


class SaveNoteTool(Tool):
    name = "save_note"
    description = "Save a note into long-term memory."
    usage = "Use ONLY when the user says 'remember' or 'save'."
    example = 'User: Remember my name is Shorif.\nAssistant:\n{"tool": "save_note", "input": "My name is Shorif"}'

    def __init__(self):
        self.repository = NoteRepository()

    def execute(self, note: str):
        self.repository.save(note)
        return "Note saved successfully."


class ListNotesTool(Tool):
    name = "list_notes"
    description = "Retrieve all saved notes."
    usage = "Use when the user asks 'what do you know about me?' or 'show my notes'."
    example = 'User: What do you know about me?\nAssistant:\n{"tool": "list_notes", "input": ""}'

    def __init__(self):
        self.repository = NoteRepository()

    def execute(self, _=None):
        notes = self.repository.list_all()
        if not notes:
            return "No notes found."
        return "\n".join(note.content for note in notes)
