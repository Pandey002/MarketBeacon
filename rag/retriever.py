# Retriever
# This module queries ChromaDB to retrieve relevant information for analysis.

import chromadb
from chromadb.config import Settings


def initialize_chromadb():
    client = chromadb.Client(Settings(
        chroma_db_impl="duckdb+parquet",
        persist_directory="./chromadb_storage"
    ))
    return client

def query_embeddings(collection_name, query_text):
    client = initialize_chromadb()
    collection = client.get_collection(name=collection_name)

    results = collection.query(
        query_texts=[query_text],
        n_results=5  # Number of results to retrieve
    )
    return results

if __name__ == "__main__":
    query_text = "What are the latest updates from competitors?"
    results = query_embeddings("competitive_intel", query_text)

    print("Query Results:")
    for result in results["documents"]:
        print(result)
        print(result)
