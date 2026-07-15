from app.tools.construction.retriever import Retriever
from app.llm.client import LLMClient


class RAGService:

    def __init__(self):
        self.retriever = Retriever()
        self.llm = LLMClient()

    def ask(self, question: str):
        results = self.retriever.retrieve(question)
        context = ""
        for result in results:
            context += f"Source: {result['source']}\n{result['text']}\n------------------\n"

        messages = [
            {
                "role": "system",
                "content": (
                    "You are a construction engineering assistant.\n"
                    "Answer ONLY using the provided context and give the source information from which document you find the answer.\n"
                    "If the answer is not in the context, say:\n"
                    "'I couldn't find that information in the provided documents.'"
                ),
            },
            {
                "role": "user",
                "content": f"Context:\n{context}\nQuestion:\n{question}",
            },
        ]
        return self.llm.chat(messages)
