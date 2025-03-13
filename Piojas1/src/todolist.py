class TodoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        if not task or not isinstance(task, str):
            raise ValueError("Task must be a non-empty string")
        self.tasks[task] = False

    def complete_task(self, task):
        if task not in self.tasks:
            raise KeyError(f"Task '{task}' does not exist")
        self.tasks[task] = True

    def get_active_tasks(self):
        return [task for task, completed in self.tasks.items() if not completed]

    def get_completed_tasks(self):
        return [task for task, completed in self.tasks.items() if completed]
