from src.utils.task_validators import TaskValidator
from src.utils.view_utils import ViewUtils
from colorama import Fore, Style 
import time
import os



class TaskView:
    
    ## Main Interface
    def show_title(self):
        print("\033[1;35m") 
        print("""
    $$$$$$\ $$\   $$\ $$$$$$$$\ $$\   $$\ $$$$$$$$\ $$$$$$$$\ 
    \_$$  _|$$$\  $$ |$$  _____|$$$\  $$ |$$  _____|\__$$  __|
    $$ |  $$$$\ $$ |$$ |      $$$$\ $$ |$$ |         $$ |   
    $$ |  $$ $$\$$ |$$$$$\    $$ $$\$$ |$$$$$\       $$ |   
    $$ |  $$ \$$$$ |$$  __|   $$ \$$$$ |$$  __|      $$ |   
    $$ |  $$ |\$$$ |$$ |      $$ |\$$$ |$$ |         $$ |   
    $$$$$$\ $$ | \$$ |$$ |      $$ | \$$ |$$$$$$$$\    $$ |   
    \______|\__|  \__|\__|      \__|  \__|\________|   \__|""")
        print('\033[0m')
    
    def show_menu(self):
        while True:
            self.show_title()
            print("\n" + "=" * 10 + " Gerenciador de Tarefas " + "=" * 10)
            print(f"{Fore.GREEN}1. Adicionar Tarefa{Style.RESET_ALL}")
            print(f"{Fore.GREEN}2. Listar Tarefas{Style.RESET_ALL}")
            print(f"{Fore.GREEN}3. Marcar Tarefa como Concluída{Style.RESET_ALL}")
            print(f"{Fore.GREEN}4. Remover Tarefa{Style.RESET_ALL}")
            print(f"{Fore.GREEN}5. Sair{Style.RESET_ALL}")
        
            try:
                choice = input(f"{Fore.YELLOW}Escolha uma opção: {Style.RESET_ALL}")
                choice_int = int(choice)
                if choice_int in range(1, 6):
                    return str(choice_int)
                else:
                    ViewUtils.display_error("Opção inválida. Tente novamente.")
            except ValueError:
                ViewUtils.display_error("Opção inválida. Tente novamente.")

    ## Prompts
    def prompt_for_create_task(self):
        title = self._get_valid_title()
        description = input("Digite uma descrição para Tarefa: (Opcional) ")
        deadline = self._get_valid_deadline()
        urgency_level = self._get_valid_urgency_level()
        return title, description, deadline, urgency_level
    
    def prompt_for_task_id(self):
        while True:
            try:
                task_id = int(input("Digite o ID da Tarefa: "))
                if task_id > 0:
                    return task_id
            except ValueError:
                ViewUtils.display_error("ID inválido. Tente novamente.")
                
    ## Displays
    def display_tasks(self, tasks_list):
        os.system('cls' if os.name == 'nt' else 'clear')
        table_header = "{:^6} | {:^6} | {:^6}".format("ID", "Status", "Title")
        table_border = "-" * len(table_header)

        print("Task List:")
        print(table_border)
        print(table_header)
        print(table_border)

        for task in tasks_list:
            task_id = str(task.id).ljust(6)
            task_status = str(task.status).ljust(6)
            task_title = str(task.title).ljust(6)
            print(f"{task_id} | {task_status} | {task_title}")

        print(table_border)
        ViewUtils.display_menu_prompt(self.show_menu)
        
            
    def display_full_task(self, task):
        print(f"ID: {task.id}, Titulo: {task.title}, Status: {task.status}")
        print(f"Data de Criação: {task.created_at} | Prazo: {task.deadline} | Urgência: {task.urgency_level}")
        print(f"Descrição: {task.description}")
        ViewUtils.display_menu_prompt(self.show_menu)
    
    def display_task_not_found(self, task_id):
        print(f"Tarefa com ID {task_id} não pode ser encontrada :(")        
        
    
    ## Validators
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
                ViewUtils.display_error("Data inválida. Data deve seguir o formato YYYY-MM-DD.Tente novamente.")
                
    def _get_valid_urgency_level(self):
        while True:
            urgency_level = input("Digite a urgência (1, 2, 3, 4 ou 5): ")
            if TaskValidator.validate_urgency_level(urgency_level):
                return urgency_level
            else:
                ViewUtils.display_error("Nível de Urgência inválida. O valor deve ser entre 1 e 5. Tente novamente.")
