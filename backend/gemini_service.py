import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"

def get_gemini_suggestions(resume_text: str, job_description: str, ats_score: int) -> dict:
    if not GEMINI_API_KEY:
        return {
            "strengths": ["Strong technical background detected."],
            "improvements": ["Add more quantified achievements."],
            "recommendations": ["Tailor resume keywords to the job description."],
        }

    prompt = f"""
You are an expert ATS resume coach. Analyze this resume against the job description.
ATS Score: {ats_score}/100

RESUME:
{resume_text[:3000]}

JOB DESCRIPTION:
{job_description[:1500]}

Respond ONLY with valid JSON (no markdown, no extra text):
{{
  "strengths": ["strength 1", "strength 2", "strength 3"],
  "improvements": ["improvement 1", "improvement 2", "improvement 3"],
  "recommendations": ["recommendation 1", "recommendation 2", "recommendation 3"]
}}
"""

    try:
        response = requests.post(
            f"{GEMINI_URL}?key={GEMINI_API_KEY}",
            json={"contents": [{"parts": [{"text": prompt}]}]},
            timeout=20,
        )
        response.raise_for_status()
        raw = response.json()["candidates"][0]["content"]["parts"][0]["text"]
        raw = raw.strip().replace("```json", "").replace("```", "").strip()
        return json.loads(raw)
    except Exception as e:
        print(f"Gemini error: {e}")
        return {
            "strengths": ["Relevant experience detected in resume."],
            "improvements": ["Include more measurable results and metrics."],
            "recommendations": ["Mirror keywords from the job description more closely."],
        }
