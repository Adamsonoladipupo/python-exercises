from fastapi import FastAPI, Body
from pydantic import BaseModel
from datetime import datetime


app = FastAPI()
todos = []

class Todo:
    _counter = 0

    def __init__(self, title: str, description: str, is_done: bool):
        Todo._counter += 1
        self.todo_id = Todo._counter
        self.title = title
        self.description = description
        self.is_done = is_done
        self.date = datetime.now()

@app.get("/todos")
def get_todo():
    return todos

@app.post("/todos")
def add_a_new_todo(new_todo: dict = Body(...)):
    new_todo = Todo(**new_todo)
    todos.append(new_todo)
    return new_todo


@app.get("/todos/{todo_id}")
def read_todo(todo_id: int):
    for existing_todo in todos:
        if existing_todo.todo_id == todo_id:
            return existing_todo
    return None


@app.delete("/todos/{todo_id}")
def read_todo(todo_id: int):
    for existing_todo in todos:
        if existing_todo.todo_id == todo_id:
            todos.remove(existing_todo)
            return "removed successfully"
    return None

@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, title: str, description: str, is_done: bool):
    for existing_todo in todos:
        if existing_todo.todo_id == todo_id:
            existing_todo.title = title
            existing_todo.description = description
            existing_todo.is_done = is_done
            return "updated successfully"
    return None


