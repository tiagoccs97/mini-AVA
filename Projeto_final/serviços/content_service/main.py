# content_service/main.py
from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
import jwt

app = FastAPI()

contents_db = {}
SECRET_KEY = "supersecret"

class Content(BaseModel):
    title: str
    description: str
    url: str

def verify_token(token: str):
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return decoded["username"]
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Token inválido ou expirado.")

@app.post("/content")
async def create_content(content: Content, authorization: str = Header(None)):
    if authorization is None:
        raise HTTPException(status_code=401, detail="Token não fornecido.")
    username = verify_token(authorization.replace("Bearer ", ""))
    content_id = len(contents_db) + 1
    contents_db[content_id] = {**content.dict(), "username": username}
    return {"content_id": content_id, "message": f"Conteúdo criado por {username}"}

@app.get("/content")
async def list_content():
    return {"contents": list(contents_db.values())}
