from app.tools.base import Tool
from app.tools.construction.rag_service import RAGService


class RAGTool(Tool):

    name = "search_construction_docs"

    description = (
        "Search construction documents "
        "to answer engineering questions."
    )

    usage = (
        "Use this tool whenever the user asks "
        "about construction, safety, materials, "
        "standards or engineering."
    )

    example = "Example: search_construction_docs('What is the minimum concrete strength for foundations?')"

    def __init__(self):
        self.rag = RAGService()

    def execute(self, query):

        return self.rag.ask(query)
