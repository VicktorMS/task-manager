# Permita ao usuário adicionar, listar, marcar como concluída e remover tarefas. 

# tarefa: ID da tarefa, descrição, data de criação, status, prazo final, urgência, entre outros atributos...

# Funcionalidades do Programa:

# Adicionar Tarefa: Permitir ao usuário adicionar uma nova tarefa à lista de tarefas pendentes.
# Listar Tarefas: Mostrar todas as tarefas pendentes na lista, enumerando-as.
# Marcar Tarefa como Concluída: Permitir ao usuário marcar uma tarefa específica como concluída.
# Remover Tarefa: Dar ao usuário a opção de remover uma tarefa da lista.

from src.task_controller import TaskController
from src.task_factory import TaskFactory
from src.task_view import TaskView


class TaskApp:
    def __init__(self):
        self.task_view = TaskView()
        self.task_controller = TaskController()
        self.task_factory = TaskFactory()
    
    def run(self):
        self.task_view.show_title()
        while True:
            choice = self.task_view.show_menu()
            if choice == "1":
                title, description, deadline, urgency_level = self.task_view.prompt_for_task()
                task = self.task_factory.create_task(title, description, deadline, urgency_level)
                self.task_controller.add_task(task)
            elif choice == "2":
                tasks = self.task_controller.list_tasks()
                self.task_view.display_tasks(tasks)
            elif choice == "3":
                task_id = self.task_view.prompt_for_task_id()
                self.task_controller.mark_task_as_complete(task_id)
            elif choice == "4":
                task_id = self.task_view.prompt_for_task_id()
                self.task_controller.remove_task(task_id)
            elif choice == "5":
                break
            else:
                print("Opcão inválida. Tente novamente.")