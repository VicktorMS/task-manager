class TaskView:
    def prompt_for_task_id(self):
        title = input("Digite o título da Tarefa: ")
        description = input(f"Digite uma descrição para '{title}': (Opcional) ")
        
        