# Criação da classe de usuário que vai ser testada

from uuid import UUID
from typing import List
from domain.Task.task_entity import Task

class User:
    id: UUID
    name: str
    task_list: List[Task]

    def __init__(self, id:UUID, name:str):
        self.id = id
        self.name = name
        self.name = name
        self.task_list = []
        self.validate()

    def validate(self):
        # Verifica o tipo de entrada
        if not isinstance(self.id,UUID):
            raise Exception("id must be an UUID")
        
        if not isinstance(self.name, str) or len(self.name) == 0:
            raise Exception("name is required")

    def collect_tasks(self, tasks:List[Task]) -> None: # Não vai retornar nada
        self.task_list.extend(tasks)
