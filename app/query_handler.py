import cohere

def ask_cohere(text: str, question: str, api_key: str) -> str:
    try:
        co = cohere.Client(api_key)

        prompt = f"""
You are a professional insurance policy assistant. You are given a policy document and a user's question.
Give a clear and precise answer based only on the content provided.

Policy Document:
{text[:10000]}

User Question:
{question}

Guidelines:
- If the answer is not explicitly stated in the document, respond with "Not mentioned."
- Be accurate and avoid making assumptions.
- Keep your answer clear, direct, and within 2–3 sentences.
"""

        response = co.generate(
            model="command",  # Use "command" not "command-r"
            prompt=prompt,
            max_tokens=300,
            temperature=0.2,
            stop_sequences=["--END--"],
        )

        return response.generations[0].text.strip()

    except Exception as e:
        return f"Error: {str(e)}"
