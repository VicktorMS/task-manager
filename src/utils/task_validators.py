from datetime import datetime

"""
Classe para validar as tarefas
"""
class TaskValidator:
    @staticmethod
    def validate_title(title):
        if len(title) > 0:
            return True
        else:
            return False
        
    @staticmethod
    def validate_date(date_str):
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
            return True
        except ValueError:
            return False
        
    @staticmethod
    def validate_urgency_level(urgency_level):
        if int(urgency_level) in range(1, 6):
            return True
        else:
            return False
    