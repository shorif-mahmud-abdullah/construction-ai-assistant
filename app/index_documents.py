from app.tools.construction.ingestion.indexer import DocumentIndexer


def main():
    indexer = DocumentIndexer()
    indexer.index_folder("documents")


if __name__ == "__main__":
    main()