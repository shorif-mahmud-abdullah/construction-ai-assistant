# Construction AI Assistant

An AI-powered assistant for construction engineering queries. Uses RAG (Retrieval-Augmented Generation) to answer questions from construction documents, with built-in tools for calculations and note-taking.

## Architecture

- **LLM**: Ollama (local inference, default model: `qwen2.5:1.5b`)
- **Embeddings**: `all-MiniLM-L6-v2` via sentence-transformers
- **Vector DB**: ChromaDB (persistent storage)
- **Database**: PostgreSQL (notes storage)
- **PDF parsing**: pypdf

## Project Structure

```
app/
├── agent/              # Core agent with multi-step tool-use loop
├── llm/                # Ollama LLM client
├── memory/             # Conversation history
├── planner/            # LLM-based planner (decides tool vs direct answer)
├── prompts/            # System prompt builder
├── tools/              # Tool registry and implementations
│   ├── base.py         # Abstract tool base class
│   ├── registry.py     # Tool registry (maps names → tools)
│   ├── calculator/     # Math expression evaluator
│   ├── construction/   # RAG search + document ingestion pipeline
│   │   ├── ingestion/  # PDF loading, chunking, indexing
│   │   ├── embedding_model.py
│   │   ├── rag_service.py
│   │   ├── retriever.py
│   │   └── vector_store.py
│   └── memory/         # PostgreSQL-backed notes (save + list)
├── config.py           # Environment configuration (dotenv)
├── application.py      # CLI entrypoint
├── main.py             # Main runner
└── index_documents.py  # Standalone document indexing script
```

## Tools

| Tool | Description |
|------|-------------|
| `calculator` | Evaluate math expressions |
| `save_note` | Persist a note to PostgreSQL |
| `list_notes` | Retrieve all saved notes |
| `search_construction_docs` | RAG search over construction documents |

## Prerequisites

- Python 3.10+
- Ollama running locally (default: `http://localhost:11434`)
- PostgreSQL database

## Configuration

Create a `.env` file in the project root:

```env
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=qwen2.5:1.5b

DB_HOST=localhost
DB_PORT=5432
DB_NAME=agent_learning
DB_USER=postgres
DB_PASSWORD=your_password

CHROMA_PATH=./chroma_db
```

## Setup

```bash
pip install -r requirements.txt
```

## Index Documents

Before querying, index the PDF documents in the `documents/` folder:

```bash
python -m app.index_documents
```

## Usage

```bash
python -m app.main
```

Type your construction-related questions and the agent will use its tools to answer. Type `exit` or `quit` to stop.
