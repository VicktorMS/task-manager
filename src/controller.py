from src.model import Task


class TaskNotFoundException(Exception):
    def __init__(self, task_id):
        self.task_id = task_id
        super().__init__(f'Task with ID {task_id} not found')
        
        def __str__(self):
            return f"TaskNotFoundException: Task with ID {self.task_id} not found"


class TaskController():
    def __init__(self) -> None:
        self.tasks = []
        
    def create_task(self, id, description, deadline, urgency_level):
        task = Task(id, description, deadline, urgency_level)
        self.tasks.append(task)
        
    def list_tasks(self):
        return self.tasks
    
    def get_task_by_id(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        raise TaskNotFoundException(task_id)
    
    def remove_task(self, task_id):
        task = self.get_task_by_id(task_id)
        self.tasks.remove(task)
        
    def mark_as_completed(self, task_id):
        task = self.get_task_by_id(task_id)
        task.mark_as_completed()
        return task
    
    
    