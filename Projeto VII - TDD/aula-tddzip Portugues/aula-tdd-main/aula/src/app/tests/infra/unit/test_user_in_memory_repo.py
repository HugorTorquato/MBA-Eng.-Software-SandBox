
from domain.User.user_entity import User
# from domain.Task.task_entity import Task
from infra.user.in_memory_user_repo import InMemoryUserRepository

from uuid import uuid4




class TestSaveUser:

    #Testar se é possível salvar user no repo
    # Teste para validar o repositório para o metodo save
    def test_Can_Save_user(self):
        repository = InMemoryUserRepository()

        user1 = User(id=uuid4(), name="Hugo")
        user2 = User(id=uuid4(), name="Tay")

        # Salva users in repository
        repository.save(user1)
        repository.save(user2)

        # Verificar se os users estão dentro do repositorio e se a lista de user tem 2 users
        assert len(repository.users) == 2
        assert repository.users[0] == user1
        assert repository.users[1] == user2


#Retornar um user pelo ID dele
class TestGetUserById:

    def test_can_get_user_by_id(self):
        repository = InMemoryUserRepository()

        user1 = User(id=uuid4(), name="Hugo")
        user2 = User(id=uuid4(), name="Tay")

        # Salva users in repository
        repository.save(user1)
        repository.save(user2)

        user = repository.get_by_id(user1.id)

        assert user == user1

    # Testar se retorna empty user if it doesn't exist
    def test_when_user_does_not_exist_should_return_none(self):
        repository = InMemoryUserRepository()

        user1 = User(id=uuid4(), name="Hugo")
        user2 = User(id=uuid4(), name="Tay")

        # Salva users in repository
        repository.save(user1)
        repository.save(user2)

        user = repository.get_by_id(userId=uuid4())

        assert user == None

class TestUpdateUser:

    #Testar pra ver se é possível atualizar o nome de um user
    def test_update_user_name(self):
        repository = InMemoryUserRepository()

        user1 = User(id=uuid4(), name="Hugo")
        user2 = User(id=uuid4(), name="Tay")

        # Salva users in repository
        repository.save(user1)
        repository.save(user2)

        new_name = "Hugoo"
        user = repository.update_name_by_id(userId=user1.id, newName=new_name)

        assert new_name == repository.get_by_id(userId=user1.id).name