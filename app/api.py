from fastapi import APIRouter
from app.retrieval import retrieve_context
from app.prompt import build_prompt
from app.llm import generate_answer

router = APIRouter()

@router.post("/query")
def query_rag(question: str):
    context = retrieve_context(question)
    prompt = build_prompt(context, question)
    answer = generate_answer(prompt)
    return {"answer": answer}
