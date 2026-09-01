from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, UploadFile, File, Form
from pydantic import BaseModel
from pypdf import PdfReader

from app.matcher import match


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class MatchRequest(BaseModel):
    cv: str
    job_description: str


@app.get("/")
def home():
    return {"message": "Job Description Matcher API"}


@app.post("/match")
def match_job(request: MatchRequest):
    score, matched_skills, missing_skills = match(
        request.cv,
        request.job_description
    )

    return {
        "match_score": score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }


@app.post("/upload-cv")
async def upload_cv(file: UploadFile = File(...)):
    reader = PdfReader(file.file)

    cv_text = ""

    for page in reader.pages:
        cv_text += page.extract_text() or ""

    return {
        "filename": file.filename,
        "cv_text": cv_text
    }


@app.post("/match-pdf")
async def match_pdf(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):
    reader = PdfReader(file.file)

    cv_text = ""

    for page in reader.pages:
        cv_text += page.extract_text() or ""

    score, matched_skills, missing_skills = match(
        cv_text,
        job_description
    )

    return {
        "filename": file.filename,
        "match_score": score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }