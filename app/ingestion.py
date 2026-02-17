from sentence_transformers import SentenceTransformer
from pypdf import PdfReader
import faiss
import os
import pickle

model = SentenceTransformer("all-MiniLM-L6-v2")

def load_documents(folder="data/documents"):
    texts = []
    for file in os.listdir(folder):
        if file.endswith(".pdf"):
            reader = PdfReader(os.path.join(folder, file))
            for page in reader.pages:
                texts.append(page.extract_text())
    return texts

def chunk_text(text, chunk_size=500, overlap=100):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size - overlap):
        chunks.append(" ".join(words[i:i + chunk_size]))
    return chunks

def build_vector_store():
    docs = load_documents()
    chunks = []
    for doc in docs:
        chunks.extend(chunk_text(doc))

    embeddings = model.encode(chunks)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    faiss.write_index(index, "vector_store/index.faiss")
    pickle.dump(chunks, open("vector_store/chunks.pkl", "wb"))
