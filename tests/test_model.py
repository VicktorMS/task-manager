from datetime import datetime
import time
import unittest

from src.model import Task


class TestTaskModel(unittest.TestCase): 
    def test_create_task(self):
        task = Task(1, "Task 1", False, "2023-05-01", 3)
        
        self.assertEqual(task.id, 1)
        self.assertEqual(task.description, "Task 1")
        self.assertEqual(task.created_at, datetime.now().strftime("%Y-%m-%d %H:%M:%S") )
        self.assertEqual(task.status, False)
        self.assertEqual(task.deadline, "2023-05-01")
        self.assertEqual(task.urgency_level, 3)
    
    def test_mark_as_completed(self):
        task = Task(1, "Task 1", False, "2023-05-01", 3)
        task.mark_as_completed()
        
        self.assertEqual(task.status, True)
        
    def test_urgency_level(self):
        task1 = Task(1, "Task 1", False, "2023-05-01", 3)
        self.assertEqual(task1.urgency_level, 3)

        with self.assertRaises(ValueError):
            Task(2, "Task 2", False, "2023-05-01", 999)
        
if __name__ == "__main__":
    unittest.main()