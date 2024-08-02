from src.utils.task_validators import TaskValidator
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
        print('Bem vindo ao gerenciador de tarefas!')
    
    def show_menu(self):
        while True:
            print("\n" + "=" * 20 + " Menu " + "=" * 20)
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
                    self.display_error("Opção inválida. Tente novamente.")
            except ValueError:
                self.display_error("Opção inválida. Tente novamente.")

    ## Task Prompts
    def prompt_for_create_task(self):
        title = self._get_valid_title()
        description = input("Digite uma descrição para Tarefa: (Opcional) ")
        deadline = self._get_valid_deadline()
        urgency_level = self._get_valid_urgency_level()
        return title, description, deadline, urgency_level
    
    def display_tasks(self, tasks):
        os.system('cls' if os.name=='nt' else 'clear')
        print("Tarefas:")
        for task in tasks:
            print(f"ID: {task.id}, Titulo: {task.title}, Status: {task.status}")
            
    def display_full_task(self, task):
        print(f"ID: {task.id}, Titulo: {task.title}, Status: {task.status}")
        print(f"Data de Criação: {task.created_at} | Prazo: {task.deadline} | Urgência: {task.urgency_level}")
        print(f"Descrição: {task.description}")

    ## Task Errors and Messages
    def display_error(self, error):
        os.system('cls' if os.name=='nt' else 'clear')
        print(error)
        time.sleep(1)
        os.system('cls' if os.name=='nt' else 'clear')
        
    
    def display_task_not_found(self, task_id):
        print(f"Tarefa com ID {task_id} não pode ser encontrada :(")        
        
    
   
    ## Validators
    def _get_valid_title(self):
        while True:
            title = input("Digite o nome da tarefa: ")
            if TaskValidator.validate_title(title):
                return title
            else:
                self.display_error("Nome inválido. Tente novamente.")
    
    def _get_valid_deadline(self):
        while True:
            deadline = input("Digite a data de conclusão (YYYY-MM-DD): ")
            if TaskValidator.validate_date(deadline):
                return deadline
            else:
                self.display_error("Data inválida. Data deve seguir o formato YYYY-MM-DD.Tente novamente.")
                
    def _get_valid_urgency_level(self):
        while True:
            urgency_level = input("Digite a urgência (1, 2, 3, 4 ou 5): ")
            if TaskValidator.validate_urgency_level(urgency_level):
                return urgency_level
            else:
                self.display_error("Nível de Urgência inválida. O valor deve ser entre 1 e 5. Tente novamente.")
