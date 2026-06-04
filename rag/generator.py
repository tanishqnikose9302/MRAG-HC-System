# LLM GENERATOR
import openai

def generate_answer(context, question):
    prompt = f"""
    Use only the context below to answer.

    Context:
    {context}

    Question:
    {question}

    Answer:
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["choices"][0]["message"]["content"]
