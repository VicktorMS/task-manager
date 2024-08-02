import time
from colorama import Fore, Style 
import os



class TaskView:
    def prompt_for_task(self):
        title = input("Digite o título da Tarefa: ")
        description = input(f"Digite uma descrição para Tarefa: (Opcional) ")
        deadline = input(f"Digite um prazo para Tarefa: (AAAA-MM-DD) ")
        urgency_level = input(f"Digite a prioridade para Tarefa: (1 a 5) ")
        
        return title, description, deadline, urgency_level
    
    def display_tasks(self, tasks):
        print("Tarefas:")
        for task in tasks:
            print(f"ID: {task.id}, Titulo: {task.title}, Status: {task.status}")
            
    def display_full_task(self, task):
        print(f"ID: {task.id}, Titulo: {task.title}, Status: {task.status}")
        print(f"Data de Criação: {task.created_at} | Prazo: {task.deadline} | Urgência: {task.urgency_level}")
        print(f"Descrição: {task.description}")
    
    def display_task_not_found(self, task_id):
        print(f"Tarefa com ID {task_id} não pode ser encontrada :(")
        
        
    def show_menu(self):
        print("\n" + "=" * 20 + " Menu " + "=" * 20)
        while True:
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
                    os.system('cls' if os.name=='nt' else 'clear')
                    print("Opção inválida. Tente novamente.", end='\n\n')
                    time.sleep(1)
            except ValueError:
                os.system('cls' if os.name=='nt' else 'clear')
                print("Opção inválida. Tente novamente.", end='\n\n')
                time.sleep(2)

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
