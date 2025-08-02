# 🧠 Code-Lunatics: Insurance Policy QA System (HackRx 6.0)

This project is an intelligent Question Answering system built with **FastAPI** and **Cohere LLM** that helps users extract precise answers from long insurance policy PDFs.

🔗 **Live Demo (Render)**: [https://code-lunatics.onrender.com](https://code-lunatics.onrender.com)  
📂 **GitHub Repo**: [TensorDevLJ/Code-Lunatics](https://github.com/TensorDevLJ/Code-Lunatics)

---

## 🚀 Features

- 🔍 Extracts clauses from uploaded PDF insurance policy documents
- 🧠 Answers user questions using **Cohere LLM** (command model)
- 🧾 Caches document responses to improve performance
- 🧪 Built with **FastAPI**, **Cohere**, and **PyMuPDF**

---

## 📁 Project Structure

```
hackrx/
├── app/
│   ├── api.py               # Main FastAPI route for /hackrx/run
│   ├── extractor.py         # PDF clause extraction logic
│   └── query_handler.py     # LLM (Cohere) querying logic
├── main.py                  # Entry point for FastAPI
├── requirements.txt         # Python dependencies
├── .env                     # API keys (not pushed)
└── README.md
```

---

## 📦 Setup Locally

### 1. Clone the Repository
```bash
git clone https://github.com/TensorDevLJ/Code-Lunatics.git
cd Code-Lunatics
```

### 2. Create and Activate Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Add `.env` file
Create a `.env` file in the root with the following:
```
COHERE_API_KEY=your_cohere_api_key
HACKRX_API_KEY=testkey123
```

### 5. Run the FastAPI Server
```bash
python main.py
```

Server will run at: `http://localhost:8000`

---

## 📬 API Usage

### Endpoint: `POST /hackrx/run`

#### Headers:
```http
Authorization: Bearer testkey123
Content-Type: application/json
```

#### Body:
```json
{
  "documents": [
    "https://hackrx.blob.core.windows.net/assets/hackrx_6/policies/BAJHLIP23020V012223.pdf"
  ],
  "questions": [
    "What is the waiting period for cataract surgery?",
    "Is maternity covered under this policy?"
  ]
}
```

#### Sample Response:
```json
{
  "answers": [
    "The waiting period for cataract surgery is 45 days under this policy.",
    "Maternity is covered under this policy..."
  ]
}
```

---

## 🌐 Deploy on Render

### 1. Push Code to GitHub
✅ Already done!

### 2. Visit: [https://render.com](https://render.com)

### 3. Deploy a New Web Service:
- Connect your GitHub repo
- **Build Command**:
  ```bash
  pip install -r requirements.txt
  ```
- **Start Command**:
  ```bash
  uvicorn main:app --host 0.0.0.0 --port $PORT
  ```
- Add Environment Variables in Render:
  ```
  COHERE_API_KEY=your_cohere_api_key
  HACKRX_API_KEY=testkey123
  ```

---

## 📜 License

This project is built for HackRx 6.0 Hackathon by Team **Code-Lunatics**.

---

## 🧠 Contributors

- 👩‍💻 Likhitha J
- 🚀 Team Code-Lunatics
