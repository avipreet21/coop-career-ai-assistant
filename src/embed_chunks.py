import json
import pickle
from pathlib import Path
from search import load_documents

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

CHUNKS_FILE = Path("data/processed/chunks.jsonl")

INDEX_FILE = Path("data/processed/faiss.index")
METADATA_FILE = Path("data/processed/chunk_metadata.pkl")

model = SentenceTransformer("all-MiniLM-L6-v2")


def create_embeddings():

    chunks = load_documents(CHUNKS_FILE)

    texts = [chunk["text"] for chunk in chunks]

    print("Generating embeddings...")

    embeddings = model.encode(texts, show_progress_bar=True)

    embeddings = np.array(embeddings).astype("float32")

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    faiss.write_index(index, str(INDEX_FILE))

    with open(METADATA_FILE, "wb") as file:
        pickle.dump(chunks, file)

    print(f"Saved FAISS index to {INDEX_FILE}")
    print(f"Saved metadata to {METADATA_FILE}")


if __name__ == "__main__":
    create_embeddings()