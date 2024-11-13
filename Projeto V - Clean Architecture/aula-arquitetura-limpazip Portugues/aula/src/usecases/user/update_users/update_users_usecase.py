
from domain.__seedwork.use_case_interface import UseCaseInterface
from domain.User.use_repository_interface import UserRepositoryInterface
from usecases.user.update_users.update_users_dto import UpdateUserInputDTO, UpdateUserOutputDTO

from domain.User.user_entity import User

class UpdateUserUseCase(UseCaseInterface):

    user_repository: UserRepositoryInterface

    def __init__(self, user_repository: UserRepositoryInterface):
        user_repository = user_repository

    def execute(self, input: UpdateUserInputDTO)-> UpdateUserOutputDTO:

        user = User(id=input.id, name= input.name)

        self.user_repository.update_user(user=user)

        return UpdateUserOutputDTO(id=user.id, name=user.name)