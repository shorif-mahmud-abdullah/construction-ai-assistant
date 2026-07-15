import os

from app.tools.construction.ingestion.loader import PDFLoader
from app.tools.construction.ingestion.chunker import TextChunker
from app.tools.construction.embedding_model import EmbeddingModel
from app.tools.construction.vector_store import VectorStore


class DocumentIndexer:

    def __init__(self):
        self.loader = PDFLoader()
        self.chunker = TextChunker()
        self.embedding_model = EmbeddingModel()
        self.vector_store = VectorStore()

    def index_folder(self, folder):
        for file in os.listdir(folder):
            if not file.endswith(".pdf"):
                continue
            path = os.path.join(folder, file)
            print(f"Indexing {file}")
            text = self.loader.load(path)
            chunks = self.chunker.chunk(text)
            embeddings = self.embedding_model.embed(chunks)
            self.vector_store.add_documents(chunks, embeddings, source=file)
