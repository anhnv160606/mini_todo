class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name):
        if not task_name.strip():
            raise ValueError("Tên công việc không được trống!")
        self.tasks.append({"name": task_name, "done": False})

    def list_tasks(self):
        if not self.tasks:
            return "Danh sách công việc trống!"

        task_list = []
        for idx, task in enumerate(self.tasks, start=1):
            status = "✓" if task["done"] else "✗"
            task_list.append(f"{idx}. {task['name']} [{status}]")
        return "\n".join(task_list)