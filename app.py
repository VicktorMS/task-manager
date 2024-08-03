# Permita ao usuário adicionar, listar, marcar como concluída e remover tarefas. 

# tarefa: ID da tarefa, descrição, data de criação, status, prazo final, urgência, entre outros atributos...

# Funcionalidades do Programa:

# Adicionar Tarefa: Permitir ao usuário adicionar uma nova tarefa à lista de tarefas pendentes.
# Listar Tarefas: Mostrar todas as tarefas pendentes na lista, enumerando-as.
# Marcar Tarefa como Concluída: Permitir ao usuário marcar uma tarefa específica como concluída.
# Remover Tarefa: Dar ao usuário a opção de remover uma tarefa da lista.

from src.task_controller import TaskController, TaskNotFoundException
from src.task_factory import TaskFactory
from src.task_view import TaskView
from src.utils.view_utils import ViewUtils


class TaskApp:
    def __init__(self, view, factory):
        self.view = view
        self.factory = factory
    
    def run(self):
        self.view.show_title()
        while True:
            choice = self.view.show_menu()
            if choice == "1":
                title, description, deadline, urgency_level = self.view.prompt_for_create_task()
                self.factory.create_task(title, description, deadline, urgency_level)
                
            elif choice == "2":
                tasks = self.factory.controller.list_tasks()
                self.view.display_tasks(tasks)
                
            elif choice == "3":
                task_id = self.view.prompt_for_task_id()
                try:
                    self.factory.controller.mark_task_as_complete(task_id)
                except TaskNotFoundException:
                    ViewUtils.display_error(f"Tarefa com ID {task_id} não foi encontrada")
                
            elif choice == "4":
                task_id = self.view.prompt_for_task_id()
                try:
                    self.factory.controller.remove_task(task_id)
                except TaskNotFoundException:
                    ViewUtils.display_error(f"Tarefa com ID {task_id} não foi encontrada")
                    
            elif choice == "5":
                break
            
task_view = TaskView()
task_controller = TaskController()
task_factory = TaskFactory()
task_app = TaskApp(task_view, task_controller, task_factory)
task_app.run()
