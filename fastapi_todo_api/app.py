from typing import Optional
from fastapi import FastAPI, Response
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Todo(BaseModel):
    id: int
    description: str
    done: Optional[bool] = False

todos: list[Todo] = []

@app.get("/")
async def root():
    return {"message", "Hello World"}

@app.post("/todos")
async def create(todo: Todo):
    todos.append(todo)
    return todo

@app.get("/todos")
async def get_all():
    return todos

@app.get("/todos/{id}")
async def get(id: int):
    for item in todos:
        if item.id == id:
            return item

@app.update("/todos/{id}")
async def update(id: int, todo: Todo):
    for item in todos:
        if item.id == id:
            item = todo
            return item

def start():
    uvicorn.run("fastapi_todo_api.app:app", reload=True)