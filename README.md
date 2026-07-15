# Construction AI Assistant

An AI-powered assistant for construction engineering queries. Uses RAG (Retrieval-Augmented Generation) to answer questions from construction documents, with built-in tools for calculations and note-taking.

## Architecture

- **LLM**: Ollama (local inference)
- **Embeddings**: `all-MiniLM-L6-v2` via sentence-transformers
- **Vector DB**: ChromaDB (persistent storage)
- **Database**: PostgreSQL (notes storage)
- **PDF parsing**: pypdf

## Project Structure

```
app/
├── agent/          # Core agent with multi-step tool-use loop
├── embeddings/     # Sentence embedding model
├── llm/            # Ollama LLM client
├── loader/         # PDF document loader
├── memory/         # Conversation history
├── rag/            # RAG service (embed → search → generate)
├── tools/          # Tool registry and implementations
│   ├── calculator.py
│   ├── save_note.py
│   ├── list_notes.py
│   └── rag_tool.py
└── vectordb/       # ChromaDB vector store
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

Create `app/config.py` with:

```python
OLLAMA_HOST = "http://localhost:11434"
OLLAMA_MODEL = "your-model-name"
```

## Setup

```bash
pip install -r requirements.txt
```

## Usage

```bash
python -m app.main
```
