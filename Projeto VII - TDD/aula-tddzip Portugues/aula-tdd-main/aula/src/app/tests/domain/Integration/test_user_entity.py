
from domain.User.user_entity import User
from domain.Task.task_entity import Task

from uuid import uuid4

class TestUserWithTasks:

    # Teste para adicionar tarefas ao usuário

    def test_collect_tasks(self):

        user = User(id=uuid4(), name="Hugo")
        task1 = Task(
                task_id = uuid4(),
                user_id=user.id, # Recebe o id do user
                title="bla",
                description="blaba",
                completed=False
            )
        
        task2 = Task(
                task_id = uuid4(),
                user_id=user.id, # Recebe o id do user
                title="bla2",
                description="blaba2",
                completed=False
            )
        
        user.collect_tasks([task1, task2])

        assert len(user.task_list) == 2
        assert task1 in user.task_list
        assert task2 in user.task_list