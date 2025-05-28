class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "done": False})

    def list_tasks(self):
        return self.tasks

    def mark_done(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["done"] = True

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]