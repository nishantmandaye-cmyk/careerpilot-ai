# 🚀 CareerPilot AI — ATS Resume Analyzer

Analyze resumes against job descriptions using NLP embeddings (Sentence Transformers) and Google Gemini AI.

---

## 📁 Project Structure

```
careerpilot-ai/
 ├── frontend/
 │   └── index.html         ← Open this in your browser
 └── backend/
     ├── app.py             ← FastAPI server
     ├── nlp_engine.py      ← Embeddings + skill detection
     ├── gemini_service.py  ← Gemini AI suggestions
     ├── .env.example       ← Copy to .env and add your key
     └── requirements.txt
```

---

## ⚡ Quick Start

### 1. Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment
cp .env.example .env
# Edit .env and add your Gemini API key
```

Get your free Gemini API key at: https://aistudio.google.com/app/apikey

### 2. Run Backend

```bash
uvicorn app:app --reload --port 8000
```

Backend runs at: http://localhost:8000

### 3. Frontend

Simply open `frontend/index.html` in your browser.

> Make sure the Backend URL in the UI shows `http://localhost:8000`

---

## 🔧 How It Works

1. **PDF Upload** → PDF.js extracts text from resume in the browser
2. **Text sent to FastAPI** → Backend receives resume text + job description
3. **Embeddings** → `all-MiniLM-L6-v2` encodes both texts
4. **Cosine Similarity** → Becomes ATS score (0–100)
5. **Skill Detection** → Compares skill pool against resume and JD
6. **Gemini AI** → Generates strengths, improvements, recommendations
7. **Results displayed** → Beautiful animated UI

---

## 🌐 Deployment

### Backend → Render.com
1. Push `backend/` folder to GitHub
2. Create new Web Service on Render
3. Set environment variable: `GEMINI_API_KEY`
4. Build command: `pip install -r requirements.txt`
5. Start command: `uvicorn app:app --host 0.0.0.0 --port $PORT`

### Frontend → Vercel / Netlify
1. Push `frontend/` folder to GitHub
2. Import on Vercel (or drag-drop on Netlify)
3. Update the Backend URL in the UI to your Render URL

---

## 🛠 Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | HTML / CSS / JavaScript |
| PDF Parsing | PDF.js |
| Backend | FastAPI + Uvicorn |
| NLP Embeddings | Sentence Transformers (all-MiniLM-L6-v2) |
| Similarity | scikit-learn cosine_similarity |
| AI Suggestions | Google Gemini 1.5 Flash |
| Deployment | Vercel + Render |

---

## 💎 Resume Description

> Built **CareerPilot AI** — a full-stack ATS resume analyzer using NLP embeddings (Sentence Transformers) for semantic resume-job matching and Google Gemini AI for intelligent optimization suggestions. Features FastAPI backend with cosine similarity scoring, skill gap detection, and a modern animated UI.
