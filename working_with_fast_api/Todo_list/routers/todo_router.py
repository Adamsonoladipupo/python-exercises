from fastapi import FastAPI,Body, APIRouter
from models.todo import Todo
from repositories.todo_repository import TodoRepository
from services.todo_service import Todo_service


app = FastAPI()

class TodoRouter:
    def __init__(self, service: Todo_service):
        self.service = service

    @app.get("/todos")
    def get_todos(self):
        todos = self.service.get_all_todos()
        return todos


