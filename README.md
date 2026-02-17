![Python](https://img.shields.io/badge/Python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![FAISS](https://img.shields.io/badge/FAISS-VectorDB-orange)
![LLM](https://img.shields.io/badge/LLM-LLaMA--3-purple)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

# 🚀 Production-Grade RAG AI Assistant

### Retrieval-Augmented Generation (RAG) API using FastAPI, FAISS, SentenceTransformers & Groq LLaMA-3

------------------------------------------------------------------------

## 📌 Overview

This project implements a production-style Retrieval-Augmented
Generation (RAG) system that delivers accurate, document-grounded
responses with low latency.

Instead of relying solely on an LLM's internal knowledge (which can
cause hallucinations), this system:

1.  Retrieves semantically relevant document chunks
2.  Injects them into a structured prompt
3.  Generates grounded responses using Groq's LLaMA-3

The architecture is modular, scalable, and LLM-agnostic --- making it
suitable for enterprise knowledge bases, AI copilots, and intelligent
search systems.

------------------------------------------------------------------------

## 🧠 System Architecture

    PDF Documents
          ↓
    Text Chunking (with overlap)
          ↓
    SentenceTransformers Embeddings
          ↓
    FAISS Vector Index
          ↓
    User Query → Query Embedding
          ↓
    Top-K Similarity Search
          ↓
    Context Injection
          ↓
    Groq LLaMA-3
          ↓
    Grounded Response

------------------------------------------------------------------------

## ✨ Key Features

-   PDF document ingestion & preprocessing pipeline\
-   Dense semantic embeddings via SentenceTransformers\
-   FAISS-based similarity search (low-latency retrieval)\
-   Prompt grounding to reduce hallucinations\
-   FastAPI REST API with automatic Swagger docs\
-   Modular, LLM-agnostic architecture\
-   Secure environment-based configuration

------------------------------------------------------------------------

## 🛠 Tech Stack

-   Python\
-   FastAPI\
-   FAISS\
-   SentenceTransformers\
-   Groq (LLaMA-3)\
-   Uvicorn\
-   Pydantic

------------------------------------------------------------------------

## 📂 Project Structure

    rag-ai-assistant/
    │
    ├── app/
    │   ├── main.py
    │   ├── ingestion.py
    │   ├── retrieval.py
    │   ├── llm.py
    │   └── config.py
    │
    ├── data/
    │   └── sample.pdf
    │
    ├── requirements.txt
    ├── .env.example
    ├── .gitignore
    └── README.md

------------------------------------------------------------------------

## ⚙️ Installation & Setup

### Clone Repository

    git clone https://github.com/yourusername/rag-ai-assistant.git
    cd rag-ai-assistant

### Create Virtual Environment

    python -m venv venv

Activate:

Mac/Linux:

    source venv/bin/activate

Windows:

    venv\Scripts\activate

### Install Dependencies

    pip install -r requirements.txt

### Configure Environment Variables

Create a `.env` file:

    GROQ_API_KEY=your_api_key_here

### Run Server

    uvicorn app.main:app --reload

Swagger Docs: http://127.0.0.1:8000/docs

------------------------------------------------------------------------

## 📡 API Endpoints

### Ingest Documents

POST `/ingest`

### Query System

POST `/query`

Example Request:

    {
      "question": "What is Retrieval-Augmented Generation?"
    }

Example Response:

    {
      "answer": "Retrieval-Augmented Generation retrieves relevant document chunks and injects them into the prompt before generating a response..."
    }

------------------------------------------------------------------------

## 🎯 Why RAG?

-   Prevents hallucinations\
-   Grounds LLM output in real data\
-   Scales to large document collections\
-   Avoids costly fine-tuning

------------------------------------------------------------------------

## 🚀 Future Improvements

-   Streaming responses\
-   Hybrid retrieval (BM25 + Dense Search)\
-   Authentication & rate limiting\
-   Docker containerization\
-   Cloud deployment\
-   Evaluation metrics (Recall@K, MRR)\
-   Redis caching

------------------------------------------------------------------------

## 🏁 One-Line Interview Summary

Built a production-ready RAG system using FastAPI and FAISS that
performs semantic search over custom documents and generates grounded
responses using Groq's LLaMA-3.
