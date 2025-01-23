
from domain.User.user_entity import User
from domain.User.user_repository_interface import UserRepositoryInterface
from application.user.create_user_use_case import CreateUserUseCase, CreateUserResponse, CreateUserRequest

from unittest.mock import MagicMock
from uuid import uuid4, UUID


# Mock são objetos que simulam outras entidades
# Muito bom para testar o código sem precisar de outras partes

class TestCreateUser:

    # Teste para criar um user com dados válidos
    def test_Create_user_with_valid_data(self):

        # Repository ( test the us case without the repository)
            # Mapear a classe e ver se os metodos foram chamados ou n

        mock_repository = MagicMock(UserRepositoryInterface)
        # se um metodo ( tipo o save() or chamado) vai ser possível saber sem ter o repositorio

        # Use case
        use_case = CreateUserUseCase(repository=mock_repository)

        # input
        request = CreateUserRequest(name="Hugo")

        # output
        response = use_case.execute(request)


        assert response.id is not None
        assert isinstance(response, CreateUserResponse)
        assert isinstance(response.id, UUID)
        assert mock_repository.save.called is True