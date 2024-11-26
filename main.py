import uuid
from fastapi import FastAPI

app = FastAPI()

@app.get("/user/{id}")
def get_user(id: uuid.UUID):
    return {"user_id": id}

@app.post("/user")
def add_user(user):
    return user

@app.put("/user/{id}")
def update_user(user_id, attr):
    return

@app.delete("/user/{id}")
def delete_user(user_id):
    return
