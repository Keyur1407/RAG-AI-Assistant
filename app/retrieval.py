import faiss
import pickle
import os
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

INDEX_PATH = "vector_store/index.faiss"
CHUNKS_PATH = "vector_store/chunks.pkl"

index = None
chunks = None


def load_vector_store():
    global index, chunks

    if not os.path.exists(INDEX_PATH) or not os.path.exists(CHUNKS_PATH):
        raise RuntimeError(
            "Vector store not found. Please ingest documents first."
        )

    index = faiss.read_index(INDEX_PATH)
    chunks = pickle.load(open(CHUNKS_PATH, "rb"))


def retrieve_context(query, k=4):
    if index is None or chunks is None:
        load_vector_store()

    query_vec = model.encode([query])
    _, indices = index.search(query_vec, k)
    return [chunks[i] for i in indices[0]]
