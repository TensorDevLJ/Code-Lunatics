import cohere

def ask_cohere(text: str, question: str, api_key: str):
    co = cohere.Client(api_key)

    prompt = f"""
You are a professional insurance policy assistant. You are given a policy document and a user's question.
Give a clear and precise answer only based on the content provided below.
Policy Document:
{text[:10000]}

Question:
{question}

Guidelines:
- If the answer is not explicitly in the policy, say "Not mentioned".
- Do not hallucinate or guess.
- Keep the answer factual, clear, and concise.
"""

    try:
        response = co.generate(
            model="command",
            prompt=prompt,
            max_tokens=300,
            temperature=0.2,
        )
        return response.generations[0].text.strip()
    except Exception as e:
        return f"Error: {e}"
