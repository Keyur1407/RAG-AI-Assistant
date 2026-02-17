import os
from dotenv import load_dotenv

load_dotenv()

print("GEMINI_API_KEY FOUND:", bool(os.getenv("GEMINI_API_KEY")))

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
TOP_K = 4
