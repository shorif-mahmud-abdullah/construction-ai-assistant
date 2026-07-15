from app.tools.construction.embedding_model import EmbeddingModel
from app.tools.construction.vector_store import VectorStore


class Retriever:

    def __init__(self):
        self.embedding_model = EmbeddingModel()
        self.vector_store = VectorStore()

    def retrieve(self, query: str, n_results: int = 3):
        query_embedding = self.embedding_model.embed([query])[0]
        results = self.vector_store.search(query_embedding, n_results=n_results)
        documents = results["documents"][0]
        metadatas = results["metadatas"][0]
        return [
            {"text": doc, "source": meta["source"]}
            for doc, meta in zip(documents, metadatas)
        ]
