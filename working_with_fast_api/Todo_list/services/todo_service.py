import uuid
from datetime import datetime

from models.todo import Todo
from repositories.todo_repository import TodoRepository


class Todo_service:
    def __init__(self, repository: TodoRepository):
        self.repository = repository

    @staticmethod
    def generate_id():
        return str(uuid.uuid4())

    def create_todo(self, title: str, description: str, is_done: bool):
        todo = Todo(todo_id = Todo_service.generate_id(), title=title, description=description, is_done=is_done, date=datetime.now())
        self.repository.add_todo(todo)

    def get_all_todos(self):
        self.repository.get_all_todos()

    def get_todo_by_id(self, todo_id: str):
        todos = self.repository.get_all_todos()
        if todo_id in todos:
            self.repository.get_todo(todo_id)
        return None

    def delete_todo(self, todo_id: str):
        todos = self.repository.get_all_todos()
        if todo_id in todos:
            self.repository.delete_todo(todo_id)
        return None







