
from uuid import UUID

class Task:
    task_id: UUID
    user_id: UUID
    title: str
    description: str
    completed: bool

    def __init__(self, task_id:UUID, user_id:UUID, title:str, description:str, completed:bool):
        self.task_id = task_id
        self.user_id = user_id
        self.title = title
        self.description = description
        self.completed = completed

        self.validation()

    def validation(self):

        if not isinstance(self.task_id, UUID):
            raise Exception("id must be an UUID")
        if not isinstance(self.user_id, UUID):
            raise Exception("user id must be an UUID")
        if not isinstance(self.title, str) or len(self.title) == 0:
            raise Exception("title is required")
        if not isinstance(self.description, str) or len(self.description) == 0:
            raise Exception("description is required")
        if not isinstance(self.completed, bool) or self.completed == True:
            raise Exception("task must be incompleted")
        
    def mark_as_completed(self):
        self.completed = True