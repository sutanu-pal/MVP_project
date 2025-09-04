from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, HttpUrl
from typing import Optional
from ai_client import generate_explanation, generate_follow_up_answer
from utils import extract_text_from_url

app = FastAPI()

# CORS configuration
origins = [
    "http://localhost:3000",      # Frontend location (adjust if needed)
    "http://127.0.0.1:3000",
    "http://localhost:5500",      # If using live-server or similar
    "http://127.0.0.1:8000",      # Optional if frontend served same origin
    "*",                         # For development, allow all origins
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # you can replace with ["*"] for dev/testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ExplanationRequest(BaseModel):
    input_text: Optional[str] = None
    input_url: Optional[HttpUrl] = None

class FollowUpRequest(BaseModel):
    original_topic: str
    question: str

@app.post("/explain")
async def explain(request: ExplanationRequest):
    if request.input_url:
        content = await extract_text_from_url(request.input_url)
        if not content:
            raise HTTPException(status_code=400, detail="Unable to fetch or extract content from URL.")
        topic = content[:1000]  # trim if content too long
    elif request.input_text:
        topic = request.input_text
    else:
        raise HTTPException(status_code=400, detail="Please provide either 'input_text' or 'input_url'.")

    explanation = generate_explanation(topic)
    return {"explanation": explanation}

@app.post("/followup")
async def followup(request: FollowUpRequest):
    answer = generate_follow_up_answer(request.original_topic, request.question)
    return {"answer": answer}
