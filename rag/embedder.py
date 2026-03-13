# Embedder
# This module takes output from all agents and stores embeddings into ChromaDB.

import chromadb
from chromadb.config import Settings
from chromadb.utils import embedding_functions


def initialize_chromadb():
    client = chromadb.Client(Settings(
        chroma_db_impl="duckdb+parquet",
        persist_directory="./chromadb_storage"
    ))
    return client

def store_embeddings(collection_name, documents):
    client = initialize_chromadb()
    collection = client.get_or_create_collection(
        name=collection_name,
        embedding_function=embedding_functions.DefaultEmbeddingFunction()
    )

    for doc in documents:
        collection.add(
            documents=[doc["content"]],
            metadatas=[doc["metadata"]],
            ids=[doc["id"]]
        )

if __name__ == "__main__":
    documents = [
        {"id": "1", "content": "Competitor A launched a new product.", "metadata": {"source": "news_agent"}},
        {"id": "2", "content": "Competitor B is hiring aggressively.", "metadata": {"source": "hiring_agent"}}
    ]

    store_embeddings("competitive_intel", documents)
    print("Embeddings stored successfully in ChromaDB.")
    print("Embeddings stored successfully in ChromaDB.")
