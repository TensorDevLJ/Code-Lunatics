import cohere

def ask_cohere(text: str, question: str, api_key: str):
    co = cohere.Client(api_key)

    prompt = f"""
You are a legal insurance policy assistant. Carefully read the policy document and answer the user's question clearly and accurately.

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
