from src.task_controller import TaskController
from src.task_model import Task


class TaskFactory():
    def __init__(self):
        self.controller = TaskController()
        self.task_counter = 1
        
    def create_task(self, title, description, deadline, urgency_level):
        self.controller.create_task(self.task_counter, title, description, deadline, urgency_level)
        self.task_counter += 1