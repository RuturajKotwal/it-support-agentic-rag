from app.services.ingestion import load_file, chunk_documents
from pathlib import Path
from app.rag.vectorstore import add_documents


docs = load_file(Path("data/sample_kb/company_it_handbook.md"))
print(f"Loaded {len(docs)} documents from file.")

chunks = chunk_documents(docs)
print(f"Created {len(chunks)} chunks from documents.")

add_documents(chunks)
print(f"Added {len(chunks)} chunks to the vector store.")