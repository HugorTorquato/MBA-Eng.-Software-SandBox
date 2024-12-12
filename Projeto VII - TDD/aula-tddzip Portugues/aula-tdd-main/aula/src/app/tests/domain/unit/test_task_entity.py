
from uuid import uuid4
from domain.Task.task_entity import Task
import pytest

class TestTask:

    #Teste para verificar o construtor da classe
    def test_task_initialization(self):

        task_id = uuid4()
        user_id = uuid4()
        title = "Estudar mais sobre testes unitários"
        description = "Os testes unitários são os mais baratos"
        completed = False

        task = Task(
            task_id = task_id,
            user_id = user_id,
            title = title,
            description = description,
            completed=completed
        )

        assert task.task_id == task_id
        assert task.user_id == user_id
        assert task.title == title
        assert task.description == description
        assert task.description == description
        assert task.completed == completed

    # Teste para validação do tipo de id
    def test_task_id_validation(self):
        user_id = uuid4()
        with pytest.raises(Exception, match="id must be an UUID"):
            Task(
                task_id = 1,
                user_id=user_id,
                title="bla",
                description="blaba",
                completed=False
            )
    
    def test_task_user_id_validation(self):
        task_id = uuid4()
        with pytest.raises(Exception, match="user id must be an UUID"):
            Task(
                task_id = task_id,
                user_id=1,
                title="bla",
                description="blaba",
                completed=False
            )

    def test_task_title_validation(self):
        task_id = uuid4()
        user_id = uuid4()
        with pytest.raises(Exception, match="title is required"):
            Task(
                task_id = task_id,
                user_id=user_id,
                title="",
                description="blaba",
                completed=False
            )
    
    def test_task_description_validation(self):
        task_id = uuid4()
        user_id = uuid4()
        with pytest.raises(Exception, match="description is required"):
            Task(
                task_id = task_id,
                user_id=user_id,
                title="blabla",
                description="",
                completed=False
            )
    
    def test_task_completed_validation(self):
        task_id = uuid4()
        user_id = uuid4()
        with pytest.raises(Exception, match="task must be incompleted"):
            Task(
                task_id = task_id,
                user_id=user_id,
                title="blabla",
                description="bla",
                completed=True
            )

    # Teste pensando em regra de negocio
    # Verificar se uma tarefa foi completada mark_As_completed

    def test_mark_as_completed(self):
            task_id = uuid4()
            user_id = uuid4()

            task = Task(
                task_id = task_id,
                user_id=user_id,
                title="bla",
                description="blaba",
                completed=False
            )

            task.mark_as_completed()

            assert task.completed == True