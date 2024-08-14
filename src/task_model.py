from datetime import datetime
# tarefa: ID da tarefa, descrição, data de criação, status, prazo final, urgência, entre outros atributos...

class Task():
    """
    Representa uma tarefa no sistema. Possui título, descrição, data de criação,
    status, prazo final e urgência.
    """

    def __init__(self, id, title, description, status, deadline, urgency_level):
        self.id = id # Poderia usar um ID aleatório para cada tarefa
        self.title = title
        self.description = description
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.status = status
        self.deadline = deadline
        self._urgency_level = None
        self.urgency_level = urgency_level

    @property
    def urgency_level(self):
        return self._urgency_level

    @urgency_level.setter
    def urgency_level(self, urgency_level):
        if not (1 <= int(urgency_level) <= 5):
            raise ValueError('Urgency level must be between 1 and 5')
        self._urgency_level = urgency_level


    def mark_as_completed(self):
        self.status = True

