import json
from pathlib import Path
from search import load_documents

OUTPUT_FILE = Path("data/processed/chunks.jsonl")

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200


def split_text(text, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP):

    chunks = []
    start = 0

    while start < len(text):

        end = start + chunk_size
        chunk = text[start:end]

        if chunk.strip():
            chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


def create_chunks():

    documents = load_documents()

    all_chunks = []

    for doc in documents:

        chunks = split_text(doc["text"])

        for i, chunk in enumerate(chunks):

            all_chunks.append({
                "chunk_id": f"{doc['file_name']}_{i}",
                "file_name": doc["file_name"],
                "path": doc["path"],
                "text": chunk
            })

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:

        for chunk in all_chunks:
            file.write(json.dumps(chunk, ensure_ascii=False) + "\n")

    print(f"Created {len(all_chunks)} chunks.")
    print(f"Saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    create_chunks()