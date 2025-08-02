from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
from typing import List
import os
from dotenv import load_dotenv
import requests
import tempfile

from app.extractor import extract_pdf
from app.query_handler import ask_cohere

# Load environment variables
load_dotenv()
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
HACKRX_API_KEY = os.getenv("HACKRX_API_KEY", "testkey123")

app = FastAPI()

# ✅ Add a simple cache dictionary
document_cache = {}

class HackRxRequest(BaseModel):
    documents: List[str]
    questions: List[str]

@app.post("/hackrx/run")
async def hackrx_run(request: HackRxRequest, authorization: str = Header(None)):
    if authorization != f"Bearer {HACKRX_API_KEY}":
        raise HTTPException(status_code=401, detail="Unauthorized")

    combined_text = ""

    for doc_url in request.documents:
        # ✅ Use cache if available
        if doc_url in document_cache:
            print(f"✔ Using cached document: {doc_url}")
            combined_text += document_cache[doc_url] + "\n"
            continue

        response = requests.get(doc_url)
        if response.status_code != 200:
            print(f"❌ Failed to fetch: {doc_url}")
            continue

        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(response.content)
            tmp_path = tmp_file.name

        extracted_clauses = extract_pdf(tmp_path)
        text = "\n".join([c['clause'] for c in extracted_clauses])

        # ✅ Save to cache
        document_cache[doc_url] = text
        combined_text += text + "\n"

    print("\n=== 🧾 Extracted Text Preview ===\n")
    print(combined_text[:1000])

    answers = []
    for question in request.questions:
        answers.append(ask_cohere(combined_text, question, COHERE_API_KEY))

    return {"answers": answers}
