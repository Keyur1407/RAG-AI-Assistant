def build_prompt(context, question):
    context_text = "\n\n".join(context)
    return f"""
Answer ONLY from the context below.
Context:
{context_text}

Question:
{question}

Answer:
"""
