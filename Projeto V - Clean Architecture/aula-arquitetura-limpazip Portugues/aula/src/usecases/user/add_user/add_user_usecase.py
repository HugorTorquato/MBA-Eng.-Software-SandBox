from domain.User.use_repository_interface import UserRepositoryInterface
from domain.__seedwork.use_case_interface import UseCaseInterface

from usecases.user.add_user.add_user_dto import AddUserInputDTO, AddUserOutputDTO
from domain.User.user_entity import User
import uuid

class AddUserUseCase(UseCaseInterface):

    user_repository: UserRepositoryInterface

    def __init__(self, user_rpeository: UserRepositoryInterface):
        self.user_repository = user_rpeository
    
    def execute(self, input: AddUserInputDTO) -> AddUserOutputDTO:

        user=User(id=uuid.uuid4(), name=input.name)
        self.user_repository.add_user(user=user)

        return AddUserOutputDTO(id=user.id, name=user.name)   