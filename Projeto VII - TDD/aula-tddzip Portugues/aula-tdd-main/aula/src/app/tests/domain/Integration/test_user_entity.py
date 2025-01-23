
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


    # Contabiliar tarefas pendentes de um user
    def test_count_pending_tasks(self):
            
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
            
            task3 = Task(
                    task_id = uuid4(),
                    user_id=user.id, # Recebe o id do user
                    title="bla3",
                    description="blaba3",
                    completed=False
                )
            
            task1.mark_as_completed()
            
            #Essas tarefas fazem parte da entidade user
            user.collect_tasks([task1, task2, task3])

            user.task_list[1].mark_as_completed()

            # Metodo para contabilizar quantas tarefas o user tem
            assert user.count_pending_tasks() == 1


    # Testar a quantidade de tarefas pendentes quando o user é criado
    def test_count_pending_tasks_empty(self):
        user = User(id=uuid4(), name="Hugo")

        assert user.count_pending_tasks() == 0

    # Testar quando todas as tasks estão completas
    def test_all_tasks_completed(self):
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

        for task in user.task_list:
             task.mark_as_completed()
        
        assert user.count_pending_tasks() == 0