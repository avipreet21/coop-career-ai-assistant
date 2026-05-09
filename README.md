# AI Co-op Career Intelligence Assistant

## Overview

AI Co-op Career Intelligence Assistant is a Retrieval-Augmented Generation (RAG) application designed to help students explore real co-op experiences, internship insights, technical interview preparation, company knowledge, and career advice using semantic search and large language models.

The project processes more than 140 co-op reflective reports and internship documents, converts them into vector embeddings using transformer models, stores those embeddings in a FAISS vector index, and retrieves semantically relevant information to generate AI-powered answers.

What makes this project valuable is that the responses are grounded in real-world co-op student experiences and perspectives rather than only generic career advice.

This project was built from scratch to better understand the internal architecture behind modern AI retrieval systems instead of relying entirely on high-level AI frameworks.

###The architecture is reusable across different document domains by replacing the source dataset

## Motivation

The idea for this project came while I was searching for co-op job opportunities. During this process, I learned that the SFU co-op program has access to many reflective reports written by previous co-op students.

These reports contain valuable student perspectives, including:

- Technical interview preparation
- Networking and Linux skills
- GitHub and project recommendations
- Resume advice
- Workplace expectations
- Communication and teamwork insights
- Company and role-specific experiences

This gave me the idea to create an AI assistant that could help students learn from past co-op experiences. Instead of manually reading many reports, users can ask questions and receive grounded answers based on relevant retrieved content.

The goal was not only to build a useful career tool, but also to understand how semantic search, embeddings, vector databases, and RAG systems work together in a real application.

---
The goal was not only to build a useful career tool, but also to understand how semantic search, embeddings, vector databases, and RAG systems work together in a real application.

## Features

### Semantic Search

Uses transformer embeddings and FAISS vector search to retrieve information based on meaning instead of exact keywords.

### AI-Generated Answers (RAG)

The application uses a Retrieval-Augmented Generation pipeline.

It combines:

Semantic retrieval
Relevant document chunks
Prompt construction
OpenAI GPT models

to generate grounded natural language answers.

Instead of asking the language model to answer from general knowledge only, the system first retrieves relevant information from the indexed co-op documents and then uses that context to generate a response.

### Streamlit Interface

The project includes an interactive Streamlit interface where users can:

Ask career-related questions
Search internship and co-op experiences
Explore retrieved document sources
View AI-generated summaries
Compare answers based on real student reflections

---

## Example Output

Question
What helped the most during co-op placement?

What helped the most during co-op placement, based on the retrieved context, includes:

Networking with team members:
Setting up one-on-one meetings with relevant team members helped students build relationships and gain advice on succeeding during the co-op term.

Self-management:
Being able to manage time, responsibilities, and workplace expectations contributed directly to success. Students who managed themselves well were often trusted with more responsibilities.

Focusing on quality over quantity:
Some students found that submitting stronger, more targeted applications was more effective than applying to many jobs without preparation.

Actively seeking feedback:
Discussing resumes with peers, coordinators, and professionals helped students improve their applications and identify better opportunities.

Exploring different tasks:
Trying different responsibilities during the co-op term helped students discover what type of work they enjoyed while still contributing to the team.

In summary, networking, self-management, quality preparation, feedback, and willingness to learn were key factors that helped students succeed during co-op placements.


It will also cite the sources it took the data from.
---

## System Architecture

```text
Documents
   ↓
Chunking
   ↓
Transformer Embeddings
   ↓
FAISS Vector Index
   ↓
Semantic Retrieval
   ↓
Prompt Construction
   ↓
OpenAI GPT Model
   ↓
AI-Generated Response
```

---

## Project Structure

```text
project/
│
├── app.py
├── requirements.txt
├── .env
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── ingest.py
│   ├── chunk.py
│   ├── embed_chunks.py
│   ├── semantic_search.py
│   └── rag_answers.py
│
└── README.md
```

---

## Core Concepts Implemented

- Semantic Search
- Embeddings
- Vector Databases
- Retrieval-Augmented Generation (RAG)
- Prompt Engineering
- Document Chunking
- Similarity Search
- Transformer Models
- LLM Application Development

---

## Technologies Used

- Python
- Streamlit
- FAISS
- Sentence Transformers
- OpenAI API
- NumPy
- Pandas

---

# Using Your Own Documents

Place your PDF or DOCX files inside:

data/raw/

Then run:

python src/ingest.py
python src/chunk.py
python src/embed_chunks.py

Finally launch:

streamlit run app.py

The system will build embeddings and allow semantic AI search over your own documents.

---

## License

This project is intended for educational and portfolio purposes.
