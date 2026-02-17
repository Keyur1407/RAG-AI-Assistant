from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_answer(prompt: str) -> str:
    if not os.getenv("GROQ_API_KEY"):
        raise ValueError("GROQ_API_KEY is not set")

    completion = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",  # ✅ STABLE + FAST
        messages=[
            {"role": "system", "content": "You are a helpful enterprise AI assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
        max_tokens=512
    )

    return completion.choices[0].message.content
