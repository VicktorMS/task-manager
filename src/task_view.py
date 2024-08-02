from colorama import Fore, Style 


class TaskView:
    def prompt_for_task_id(self):
        title = input("Digite o título da Tarefa: ")
        description = input(f"Digite uma descrição para Tarefa: (Opcional) ")
        deadline = input(f"Digite um prazo para Tarefa: (AAAA-MM-DD) ")
        urgency_level = input(f"Digite uma descrição para Tarefa: (Opcional) ")
        
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
        print(f"{Fore.GREEN}1. Adicionar Tarefa{Style.RESET_ALL}")
        print(f"{Fore.GREEN}2. Listar Tarefas{Style.RESET_ALL}")
        print(f"{Fore.GREEN}3. Marcar Tarefa como Concluída{Style.RESET_ALL}")
        print(f"{Fore.GREEN}4. Remover Tarefa{Style.RESET_ALL}")
        print(f"{Fore.GREEN}5. Sair{Style.RESET_ALL}")
        return input(f"{Fore.YELLOW}Escolha uma opção: {Style.RESET_ALL}")
