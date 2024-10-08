import sys
from src.task_controller import TaskController, TaskNotFoundException
from src.task_factory import TaskFactory
from src.task_view import TaskView
from src.utils.view_utils import ViewUtils


class TaskApp:
    def __init__(self, view, factory):
        self.view = view
        self.factory = factory

    def run(self):
        while True:
            self.view.show_title()
            self.handle_user_choice()

    def handle_user_choice(self):
        choice = self.view.show_menu()
        if choice == "1":
            self.create_task()
        elif choice == "2":
            self.list_tasks()
        elif choice == "3":
            self.mark_task_as_completed()
        elif choice == "4":
            self.remove_task()
        elif choice == "5":
            self.display_full_task()
        elif choice == "0":
            self.exit_application()
            return

    def create_task(self):
        title, description, deadline, urgency_level = self.view.prompt_for_create_task()
        self.factory.create_task(title, description, deadline, urgency_level)

    def list_tasks(self):
        tasks = self.factory.controller.list_tasks()
        self.view.display_tasks(tasks)

    def mark_task_as_completed(self):
        task_id = self.view.prompt_for_task_id()
        try:
            self.factory.controller.mark_task_as_complete(task_id)
            self.view.display_success_message(f"Parabéns! você cumpriu a tarefa {task_id} !")
        except TaskNotFoundException:
            ViewUtils.display_error(f"Tarefa com ID {task_id} não foi encontrada")

    def remove_task(self):
        task_id = self.view.prompt_for_task_id()
        try:
            self.factory.controller.remove_task(task_id)
            self.view.display_success_message(f"Tarefa com ID {task_id} removida com sucesso!")
        except TaskNotFoundException:
            ViewUtils.display_error(f"Tarefa com ID {task_id} não foi encontrada")
            
    def display_full_task(self):
        task_id = self.view.prompt_for_task_id()
        try:
            task = self.factory.controller.get_task_by_id(task_id)
            self.view.display_full_task(task)
        except TaskNotFoundException:
            ViewUtils.display_error(f"Tarefa com ID {task_id} não foi encontrada")
    
    def exit_application(self):
        self.view.display_success_message(f"Obrigado, volte sempre!")
        sys.exit(0)


task_view = TaskView()
task_factory = TaskFactory()
task_app = TaskApp(task_view, task_factory)
task_app.run()

