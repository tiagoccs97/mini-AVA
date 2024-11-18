# course_service/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI()

courses_db = {}

class Course(BaseModel):
    title: str
    description: str
    content_ids: List[int]

@app.post("/course")
async def create_course(course: Course):
    course_id = len(courses_db) + 1
    courses_db[course_id] = course.dict()
    return {"course_id": course_id, "message": "Curso criado com sucesso!"}

@app.get("/course/{course_id}")
async def get_course(course_id: int):
    course = courses_db.get(course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Curso não encontrado.")
    return course
