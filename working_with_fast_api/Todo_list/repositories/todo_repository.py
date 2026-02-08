from models.todo import Todo

class TodoRepository:
    def __init__(self):
        self._todos = []

    def add_todo(self, todo: Todo):
        if self.__is_todo_new(todo):
            self.__save_todo(todo)
        else:
            self.__update_todo(todo)

    def get_all_todos(self):
        return self._todos

    def get_todo(self, todo_id: str):
        return self._todos[todo_id]

    def delete_todo(self, todo_id: str):
        del self._todos[todo_id]


    def __update_todo(self, new_todo: Todo):
        self._todos[self._todo_id] = new_todo

    def __is_todo_new(self, todo: Todo):
        for existing_todo in self._todos:
            if existing_todo.id == todo.todo_id:
                return True
        return False

    def __save_todo(self, todo : Todo):
        self._todos.append(todo)
