from src.task_controller import TaskController
from src.task_model import Task


class TaskFactory():
    def __init__(self):
        self.controller = TaskController()
        self.task_counter = 0
        
    def create_task(self, title, description, deadline, urgency_level):
        task = Task(self.task_counter, title, description, False, deadline, urgency_level)
        self.task_counter += 1
        return task