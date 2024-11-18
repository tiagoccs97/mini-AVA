# assessment_service/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI()

assessments_db = {}

class Assessment(BaseModel):
    course_id: int
    questions: List[Dict[str, str]]

@app.post("/assessment")
async def create_assessment(assessment: Assessment):
    assessment_id = len(assessments_db) + 1
    assessments_db[assessment_id] = assessment.dict()
    return {"assessment_id": assessment_id, "message": "Avaliação criada com sucesso!"}

@app.get("/assessment/{assessment_id}")
async def get_assessment(assessment_id: int):
    assessment = assessments_db.get(assessment_id)
    if not assessment:
        raise HTTPException(status_code=404, detail="Avaliação não encontrada.")
    return assessment
