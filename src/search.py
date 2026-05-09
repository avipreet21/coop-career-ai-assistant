import json
from pathlib import Path

Data_file = Path("data/processed")

def search_documents(query, document):
    results = []
    for doc in document:
        if query.lower() in doc["text"].lower():
            score = doc["text"].lower().count(query.lower())


            results.append({"document": doc,"score": score})
    results.sort(key=lambda x: x["score"], reverse=True)
    return results

def load_documents():
    with open(Data_file, "r", encoding="utf-8") as file:
        documents = [json.loads(line) for line in file]

    return documents


query = input("Enter your search query: ")
results = search_documents(query, document)
if results:
    print(f"Found {len(results)} matching documents:")
    for result in results:
        print(f"Document: {result['document']['file_name']}, Score: {result['score']}")

