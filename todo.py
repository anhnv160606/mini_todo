class TodoList:
    def __init__(self):
        self.tasks = []  # Danh sách công việc

    def add_task(self, task_name):
        """Thêm công việc mới vào danh sách"""
        if not task_name.strip():
            raise ValueError("Tên công việc không được trống!")
        self.tasks.append({
            "name": task_name,
            "done": False  # Mặc định chưa hoàn thành
        })
        return f"Đã thêm công việc: '{task_name}'"