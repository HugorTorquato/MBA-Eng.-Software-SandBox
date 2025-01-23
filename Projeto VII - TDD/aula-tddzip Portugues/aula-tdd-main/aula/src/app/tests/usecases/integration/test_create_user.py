
from domain.User.user_entity import User
from domain.User.user_repository_interface import UserRepositoryInterface
from application.user.create_user_use_case import CreateUserUseCase, CreateUserResponse, CreateUserRequest
from infra.user.in_memory_user_repo import InMemoryUserRepository


# from unittest.mock import MagicMock
from uuid import uuid4, UUID


# Mock são objetos que simulam outras entidades
# Muito bom para testar o código sem precisar de outras partes

class TestCreateUser:

    # Teste para criar um user com dados válidos
    def test_Create_user_with_valid_data(self):

        # Repository ( test the us case without the repository)
            # Mapear a classe e ver se os metodos foram chamados ou n

        repository = InMemoryUserRepository()
        # se um metodo ( tipo o save() or chamado) vai ser possível saber sem ter o repositorio

        # Use case
        use_case = CreateUserUseCase(repository=repository)

        # input
        request = CreateUserRequest(name="Hugo")

        # output
        response = use_case.execute(request)


        assert len(repository.users)
        assert isinstance(response.id, UUID)
        assert repository.users[0].id == response.id
        assert repository.users[0].name == "Hugo"