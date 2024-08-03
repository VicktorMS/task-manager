from src.task_model import Task


class TaskNotFoundException(Exception):
    def __init__(self, task_id):
        self.task_id = task_id
        super().__init__(f'Task with ID {task_id} not found')
        
        def __str__(self):
            return f"TaskNotFoundException: Task with ID {self.task_id} not found"


class TaskController():
    def __init__(self) -> None:
        self.tasks_list = []
        
    def create_task(self, id, title, description, deadline, urgency_level):
        task = Task(id, title, description, False, deadline, urgency_level)
        self.tasks_list.append(task)
        
    def list_tasks(self):
        return self.tasks_list
    
    def get_task_by_id(self, task_id):
        for task in self.tasks_list:
            if task.id == task_id:
                return task
        raise TaskNotFoundException(task_id)
    
    def remove_task(self, task_id):
        task = self.get_task_by_id(task_id)
        self.tasks_list.remove(task)
        
    def mark_task_as_complete(self, task_id):
        task = self.get_task_by_id(task_id)
        task.mark_as_completed()
        return task
    
    
    