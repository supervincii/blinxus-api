import uuid
from fastapi import FastAPI
from schema import User, Favorites

app = FastAPI()

@app.get("/user/{id}")
def get_user(id: uuid.UUID):
    return {"user_id": id}

@app.post("/user")
def add_user(user: User):
    return user
