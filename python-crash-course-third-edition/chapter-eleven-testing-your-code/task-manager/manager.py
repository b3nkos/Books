from task import Task


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        self.tasks.append(Task(title))

    def complete_task(self, index):
        if index < 0 or index >= len(self.tasks):
            raise IndexError
        
        self.tasks[index].completed = True

    def get_pending_tasks(self):
        return [task for task in self.tasks if not task.complete]
