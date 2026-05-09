from dotenv import load_dotenv
from openai import OpenAI

from src.semantic_search import semantic_search

load_dotenv()

client = OpenAI()


def build_context(results):
    context_parts = []

    for i, result in enumerate(results, start=1):
        context_parts.append(
            f"""
Source {i}
File: {result['file_name']}
Text:
{result['text']}
"""
        )

    return "\n".join(context_parts)


def generate_answer(question, top_k=5):
    results = semantic_search(question, top_k=top_k)
    context = build_context(results)

    prompt = f"""
You are an AI co-op career assistant.

Answer the user's question using ONLY the context below.
If the answer is not in the context, say you could not find enough information.

Question:
{question}

Context:
{context}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    answer = response.choices[0].message.content

    return answer, results


if __name__ == "__main__":
    question = input("Ask a question: ")

    answer, sources = generate_answer(question)

    print("\nAnswer:")
    print(answer)

    print("\nSources:")
    for source in sources:
        print("-", source["file_name"])