
from domain.__seedwork.use_case_interface import UseCaseInterface
from domain.User.use_repository_interface import UserRepositoryInterface
from usecases.user.list_users.list_users_dto import ListUserInputDTO, ListUserOutputDTO, UserDto

# Interface e DTOs importados

# Definição dos contrator - tem como dependencia o contrato
class ListUsertsUseCase(UseCaseInterface):

    user_repository: UserRepositoryInterface

    def __init__(self, user_repository: UserRepositoryInterface):
        self.user_repository = user_repository

    def execute(self, input: ListUserInputDTO) -> ListUserOutputDTO:
        users = self.user_repository.list_users()
        # Retorna uma lista de usuários

        # Recebe uma lista de entidades e precisamos passar nos contratos os
        # dados de forma mais primitivas possíveis

        # Um DTO ontermediário - usado para criar os objetos de transferencia

        # Nesse caso, passa a lista de usuarios como formato primitivo
        output = []

        for user in users:

            user_dto = UserDto(id=user.id, name=user.name)

            output.append(user_dto)

        return ListUserOutputDTO(users=output)
