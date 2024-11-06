from domain.__seedwork.user_case_interface import UseCaseInterface
from domain.User.user_repository_interface import UserRepositoryInterface

from usecases.user.find_user.find_user_dto import FindUserInputDTO, FindUserOutputDTO
from domain.User.user_entity import User
import uuid

class FindUserUseCase(UseCaseInterface):

    user_repository: UserRepositoryInterface

    def __init__(self, user_repository: UserRepositoryInterface):
        self.user_repository = user_repository

    def execute(self, input: FindUserInputDTO) -> FindUserOutputDTO:

        user = self.user_repository.find_user(user_id=input.id)

        return FindUserOutputDTO(id=user.id, name=user.name)