# user_service/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import bcrypt
import jwt

app = FastAPI()

# Banco de dados em memória
users_db = {}

SECRET_KEY = "supersecret"

class User(BaseModel):
    username: str
    password: str

@app.post("/register")
async def register(user: User):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="Usuário já existe.")
    hashed_password = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())
    users_db[user.username] = hashed_password
    return {"message": "Usuário registrado com sucesso!"}

@app.post("/login")
async def login(user: User):
    stored_password = users_db.get(user.username)
    if not stored_password or not bcrypt.checkpw(user.password.encode(), stored_password):
        raise HTTPException(status_code=401, detail="Credenciais inválidas.")
    token = jwt.encode({"username": user.username}, SECRET_KEY, algorithm="HS256")
    return {"token": token}
