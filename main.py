from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random

app = FastAPI()  # ✅ This line is critical

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class NoteRequest(BaseModel):
    name: str
    age: int
    findings: list[str]

class ICDRequest(BaseModel):
    text: str

@app.get("/")
def root():
    return {"message": "Backend is running!"}

@app.get("/dashboard")
def get_dashboard():
    return {
        "images_enhanced": 136,
        "notes_generated": 67,
        "icd_codes": 40,
        "active_patients": 6,
        "uptime": "98%"
    }

@app.post("/generate-note")
def generate_note(req: NoteRequest):
    return {"note": f"SOAP Note for {req.name}"}

@app.post("/suggest-icd")
def suggest_icd(req: ICDRequest):
    codes = ["J45.909", "E11.9", "I10"]
    return {"suggestions": [{"code": code, "confidence": 0.9} for code in codes]}

@app.get("/patients")
def get_patients():
    return [
        {"id": "P001", "name": "Dr. Saadhana", "age": 45},
        {"id": "P002", "name": "John Smith", "age": 30},
        {"id": "P003", "name": "Emma Johnson", "age": 28}
    ]