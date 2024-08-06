# import unittest

# from src.controller import TaskController
# from src.task_controller import TaskNotFoundException

# class TestTaskController(unittest.TestCase):
#     def test_get_data(self):
#         # Cria uma instância do controller
#         controller = TaskController()
        
#         # Verifica se o resultado é o esperado
#         self.assertEqual(result, "expected_result")

#     def test_create_task(self):
#         controller = TaskController()
#         id = 1
#         title = "Test Task"
#         description = "This is a test task"
#         deadline = "2023-05-01"
#         urgency_level = 3
#         controller.create_task(id, title, description, deadline, urgency_level)
#         task = controller.get_task_by_id(id)
#         self.assertEqual(task.id, id)
#         self.assertEqual(task.title, title)
#         self.assertEqual(task.description, description)
#         self.assertEqual(task.deadline, deadline)
#         self.assertEqual(task.urgency_level, urgency_level)

#     def test_list_tasks(self):
#         controller = TaskController()
#         id = 1
#         title = "Test Task"
#         description = "This is a test task"
#         deadline = "2023-05-01"
#         urgency_level = 3
#         controller.create_task(id, title, description, deadline, urgency_level)
#         tasks = controller.list_tasks()
#         self.assertEqual(len(tasks), 1)
#         self.assertEqual(tasks[0].id, id)
#         self.assertEqual(tasks[0].title, title)
#         self.assertEqual(tasks[0].description, description)
#         self.assertEqual(tasks[0].deadline, deadline)
#         self.assertEqual(tasks[0].urgency_level, urgency_level)

#     def test_get_task_by_id(self):
#         controller = TaskController()
#         id = 1
#         title = "Test Task"
#         description = "This is a test task"
#         deadline = "2023-05-01"
#         urgency_level = 3
#         controller.create_task(id, title, description, deadline, urgency_level)
#         task = controller.get_task_by_id(id)
#         self.assertEqual(task.id, id)
#         self.assertEqual(task.title, title)
#         self.assertEqual(task.description, description)
#         self.assertEqual(task.deadline, deadline)
#         self.assertEqual(task.urgency_level, urgency_level)

#     def test_remove_task(self):
#         controller = TaskController()
#         id = 1
#         title = "Test Task"
#         description = "This is a test task"
#         deadline = "2023-05-01"
#         urgency_level = 3
#         controller.create_task(id, title, description, deadline, urgency_level)
#         controller.remove_task(id)
#         with self.assertRaises(TaskNotFoundException):
#             controller.get_task_by_id(id)

#     def test_mark_task_as_complete(self):
#         controller = TaskController()
#         id = 1
#         title = "Test Task"
#         description = "This is a test task"
#         deadline = "2023-05-01"
#         urgency_level = 3
#         controller.create_task(id, title, description, deadline, urgency_level)
#         controller.mark_task_as_complete(id)
#         task = controller.get_task_by_id(id)
#         self.assertEqual(task.status, True)

#     def test_get_task_by_id_not_found(self):
#         controller = TaskController()
#         with self.assertRaises(TaskNotFoundException):
#             controller.get_task_by_id(1)

#     def test_remove_task_not_found(self):
#         controller = TaskController()
#         with self.assertRaises(TaskNotFoundException):
#             controller.remove_task(1)

#     def test_mark_task_as_complete_not_found(self):
#         controller = TaskController()
#         with self.assertRaises(TaskNotFoundException):
#             controller.mark_task_as_complete(1)
#     unittest.main()