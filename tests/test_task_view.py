import unittest
from src.task_view import TaskView

class TestTaskView(unittest.TestCase):
    def test_display_tasks(self):
        tv = TaskView()
        tv.show_title()
        tv.show_menu()
        pass