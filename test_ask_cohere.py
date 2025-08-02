import os
from app.query_handler import ask_cohere
from dotenv import load_dotenv

# Load your API key from the .env file
load_dotenv()
api_key = os.getenv("COHERE_API_KEY")

# Simulated short policy text
sample_policy_text = """
This insurance policy provides coverage for cataract surgery after a mandatory waiting period of 45 days.
It does not cover maternity expenses.
Organ donor expenses are only covered if explicitly stated in the policy schedule.
"""

# Sample user question
sample_question = "What is the waiting period for cataract surgery?"

# Call the function
answer = ask_cohere(sample_policy_text, sample_question, api_key)

# Print the result
print("\n=== ❓Question ===")
print(sample_question)
print("\n=== ✅Answer ===")
print(answer)
