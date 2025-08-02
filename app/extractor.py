import fitz

def extract_pdf(pdf_path):
    data = []
    doc = fitz.open(pdf_path)
    for page in doc:
        text = page.get_text()
        for i, clause in enumerate(text.split("\n")):
            if clause.strip():
                data.append({"clause_id": i, "clause": clause.strip()})
    return data