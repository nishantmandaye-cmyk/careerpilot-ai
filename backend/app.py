from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from nlp_engine import compute_ats_score, find_skills
from gemini_service import get_gemini_suggestions

app = FastAPI(title="CareerPilot AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class AnalyzeRequest(BaseModel):
    resume_text: str
    job_description: str

@app.get("/")
def root():
    return {"status": "CareerPilot AI is running"}

@app.post("/analyze")
def analyze(req: AnalyzeRequest):
    if not req.resume_text.strip() or not req.job_description.strip():
        raise HTTPException(status_code=400, detail="Resume text and job description are required.")

    ats_score = compute_ats_score(req.resume_text, req.job_description)
    matched_skills, missing_skills = find_skills(req.resume_text, req.job_description)
    suggestions = get_gemini_suggestions(req.resume_text, req.job_description, ats_score)

    return {
        "ats_score": ats_score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "strengths": suggestions.get("strengths", []),
        "improvements": suggestions.get("improvements", []),
        "recommendations": suggestions.get("recommendations", []),
    }
