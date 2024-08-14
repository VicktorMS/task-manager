from src.utils.task_validators import TaskValidator
from src.utils.view_utils import ViewUtils
from colorama import Fore, Style
import time


class TaskView:

    def __init__(self):
        self.menu_options = {
            1: "Adicionar Tarefa",
            2: "Listar Tarefas",
            3: "Marcar Tarefa como Concluída",
            4: "Remover Tarefa",
            5: "Visualizar uma Tarefa",
            0: "Sair"
        }

    # Métodos para exibição de informações
    def show_title(self):
        print("\033[1;35m")
        print("""$$$$$$\ $$\   $$\ $$$$$$$$\ $$\   $$\ $$$$$$$$\ $$$$$$$$\ 
\_$$  _|$$$\  $$ |$$  _____|$$$\  $$ |$$  _____|\__$$  __|
  $$ |  $$$$\ $$ |$$ |      $$$$\ $$ |$$ |         $$ |   
  $$ |  $$ $$\$$ |$$$$$\    $$ $$\$$ |$$$$$\       $$ |   
  $$ |  $$ \$$$$ |$$  __|   $$ \$$$$ |$$  __|      $$ |   
  $$ |  $$ |\$$$ |$$ |      $$ |\$$$ |$$ |         $$ |   
$$$$$$\ $$ | \$$ |$$ |      $$ | \$$ |$$$$$$$$\    $$ |   
\______|\__|  \__|\__|      \__|  \__|\________|   \__|""")
        print('\033[0m')

    def show_menu(self):
        self.clear_screen()
        self.show_title()
        self.print_title()
        self.print_menu_options()
        return self.get_user_choice(len(self.menu_options))

    def clear_screen(self):
        ViewUtils.console_clean()

    def print_title(self):
        print("\n" + "=" * 10 + " Gerenciador de Tarefas " + "=" * 10)

    def print_menu_options(self):
        for key, value in self.menu_options.items():
            print(f"{Fore.GREEN}{key}. {value}{Style.RESET_ALL}")

    def display_tasks(self, tasks_list):
        self.clear_screen()
        self.print_title()
        self.print_task_list(tasks_list)
        ViewUtils.display_menu_prompt(self.show_menu)

    def display_full_task(self, task):
        self.clear_screen()
        self.print_title()
        self.print_task_detail(task)
        ViewUtils.display_menu_prompt(self.show_menu)

    def display_task_not_found(self, task_id):
        self.clear_screen()
        self.print_title()
        print(f"Tarefa com ID {task_id} não pode ser encontrada :(")
        ViewUtils.display_menu_prompt(self.show_menu)

    def display_success_message(self, message):
        ViewUtils.console_clean()
        print(f"{Style.BRIGHT}{Fore.GREEN}{message}{Style.RESET_ALL}")
        time.sleep(1)
        ViewUtils.console_clean()

    # Métodos de entrada do usuário
    def get_user_choice(self, options_range=6):
        while True:
            try:
                choice = input(f"{Fore.YELLOW}Escolha uma opção: {Style.RESET_ALL}")
                choice_int = int(choice)
                if choice_int in range(0, options_range):
                    return str(choice_int)
                else:
                    ViewUtils.display_error("Opção inválida. Tente novamente.")
            except ValueError:
                ViewUtils.display_error("Opção inválida. Tente novamente.")

    def prompt_for_create_task(self):
        title = self._get_valid_title()
        description = input("Digite uma descrição para Tarefa: (Opcional) ")
        deadline = self._get_valid_deadline()
        urgency_level = self._get_valid_urgency_level()
        return title, description, deadline, urgency_level

    def prompt_for_task_id(self):
        ViewUtils.console_clean()
        while True:
            try:
                task_id = int(input("Digite o ID da Tarefa: "))
                if task_id > 0:
                    return task_id
            except ValueError:
                ViewUtils.display_error("ID inválido. Tente novamente.")

    # Métodos auxiliares para validação de dados
    def _get_valid_title(self):
        while True:
            title = input("Digite o nome da tarefa: ")
            if TaskValidator.validate_title(title):
                return title
            else:
                ViewUtils.display_error("Nome inválido. Tente novamente.")

    def _get_valid_deadline(self):
        while True:
            deadline = input("Digite a data de conclusão (YYYY-MM-DD): ")
            if TaskValidator.validate_date(deadline):
                return deadline
            else:
                ViewUtils.display_error("Data inválida. Data deve seguir o formato YYYY-MM-DD. Tente novamente.")

    def _get_valid_urgency_level(self):
        while True:
            urgency_level = input("Digite a urgência (1, 2, 3, 4 ou 5): ")
            if TaskValidator.validate_urgency_level(urgency_level):
                return urgency_level
            else:
                ViewUtils.display_error("Nível de Urgência inválida. O valor deve ser entre 1 e 5. Tente novamente.")

    # Metodos para exibição de detalhes da tarefa
    def print_task_list(self, tasks_list):
        table_header = "{:^6} | {:^6} | {:^6}".format("ID", "Status", "Title")
        table_border = "-" * len(table_header)

        print(table_border)
        print(table_header)
        print(table_border)

        for task in tasks_list:
            self.print_task(task)

        print(table_border)

    def print_task(self, task):
        task_id = str(task.id).ljust(6)
        task_status = str(task.status).ljust(6)
        task_title = str(task.title).ljust(6)
        print(f"{task_id} | {task_status} | {task_title}")

    def print_task_detail(self, task):
        print(f"ID: {task.id}, Titulo: {task.title}, Status: {task.status}")
        print(f"Data de Criação: {task.created_at} | Prazo: {task.deadline} | Urgência: {task.urgency_level}")
        print(f"Descrição: {task.description}\n\n")

