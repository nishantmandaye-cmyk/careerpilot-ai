from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import re

model = SentenceTransformer("all-MiniLM-L6-v2")

SKILL_POOL = [
    "python", "javascript", "typescript", "java", "c++", "c#", "go", "rust", "kotlin", "swift",
    "react", "vue", "angular", "next.js", "nuxt", "svelte", "html", "css", "tailwind",
    "node.js", "express", "fastapi", "django", "flask", "spring boot", "graphql", "rest api",
    "postgresql", "mysql", "mongodb", "redis", "elasticsearch", "firebase", "supabase",
    "docker", "kubernetes", "aws", "gcp", "azure", "terraform", "ci/cd", "github actions",
    "machine learning", "deep learning", "tensorflow", "pytorch", "scikit-learn", "pandas",
    "numpy", "nlp", "computer vision", "llm", "langchain", "openai", "hugging face",
    "git", "linux", "bash", "agile", "scrum", "jira", "figma", "data structures", "algorithms",
]

def compute_ats_score(resume_text: str, job_description: str) -> int:
    embeddings = model.encode([resume_text, job_description])
    score = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
    # Scale to 0-100 and clamp
    scaled = int(round(float(score) * 100))
    return max(0, min(100, scaled))

def normalize(text: str) -> str:
    return re.sub(r"[^a-z0-9\.\+\# ]", " ", text.lower())

def find_skills(resume_text: str, job_description: str):
    resume_norm = normalize(resume_text)
    jd_norm = normalize(job_description)

    jd_skills = [s for s in SKILL_POOL if s in jd_norm]
    if not jd_skills:
        jd_skills = SKILL_POOL  # fallback: check all

    matched = [s for s in jd_skills if s in resume_norm]
    missing = [s for s in jd_skills if s not in resume_norm]

    return matched[:20], missing[:20]
