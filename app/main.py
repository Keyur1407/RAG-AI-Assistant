from dotenv import load_dotenv
import os
load_dotenv(dotenv_path=os.path.join(os.getcwd(), ".env"))
print("DEBUG → GROQ_API_KEY FOUND:", bool(os.getenv("GROQ_API_KEY")))

from fastapi import FastAPI
from app.api import router
from app.ingestion import build_vector_store
import uvicorn



app = FastAPI(title="RAG AI Assistant")

@app.on_event("startup")
def startup():
    build_vector_store()


app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="127.0.0.1",
        port=8000,
        reload=False
    )