import unittest
from src.task_view import TaskView
from src.task_model import Task
from src.utils.view_utils import ViewUtils

class TestTaskView(unittest.TestCase):
    # def test_display_tasks(self):
    #     tv = TaskView()
    #     tasks = [
    #         Task(1, "Task 1", "Description 1", False, "2022-01-01", 1),
    #         Task(2, "Task 2", "Description 2", True, "2022-02-01", 2),
    #         Task(3, "Task 3", "Description 3", False, "2022-03-01", 3),
    #         Task(4, "Task 4", "Description 4", True, "2022-04-01", 4),
    #         Task(5, "Task 5", "Description 5", False, "2022-05-01", 5)  
    #      ]
        
    #     tv.display_tasks(tasks)
    #     pass
    
    def test_display_tasks(self):
        tv = TaskView()
        tasks = [
            Task(1, "Task 1", "Description 1", False, "2022-01-01", 1),
            Task(2, "Task 2", "Description 2", True, "2022-02-01", 2),
            Task(3, "Task 3", "Description 3", False, "2022-03-01", 3),
            Task(4, "Task 4", "Description 4", True, "2022-04-01", 4),
            Task(5, "Task 5", "Description 5", False, "2022-05-01", 5)  
         ]
        
        # tv.display_tasks(tasks)
        tv.display_tasks(tasks)
        pass
