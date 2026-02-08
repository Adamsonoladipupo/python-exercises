from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime


app = FastAPI()

class Todo:
    def __init__(self, todo_id: str, title: str, description: str, is_done: bool, date: datetime):
        self.todo_id = todo_id
        self.title = title
        self.description = description
        self.is_done = is_done
        self.date = date


