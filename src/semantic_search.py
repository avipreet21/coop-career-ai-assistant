import pickle
from pathlib import Path

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

INDEX_FILE = Path("data/processed/faiss.index")
METADATA_FILE = Path("data/processed/chunk_metadata.pkl")

model_name = "all-MiniLM-L6-v2"


def load_index_and_metadata():
    index = faiss.read_index(str(INDEX_FILE))

    with open(METADATA_FILE, "rb") as file:
        chunks = pickle.load(file)

    return index, chunks


def semantic_search(query, top_k=5):
    model = SentenceTransformer(model_name)

    index, chunks = load_index_and_metadata()

    query_embedding = model.encode([query])
    query_embedding = np.array(query_embedding).astype("float32")

    distances, indices = index.search(query_embedding, top_k)

    results = []

    for distance, idx in zip(distances[0], indices[0]):
        chunk = chunks[idx]

        results.append({
            "score": float(distance),
            "chunk_id": chunk["chunk_id"],
            "file_name": chunk["file_name"],
            "path": chunk["path"],
            "text": chunk["text"]
        })

    return results


if __name__ == "__main__":
    query = input("Enter semantic search query: ")

    results = semantic_search(query)

    for i, result in enumerate(results, start=1):
        print(f"\nResult {i}")
        print(f"File: {result['file_name']}")
        print(f"Distance: {result['score']}")
        print(f"Path: {result['path']}")
        print(result["text"][:500])
        print("-" * 80)