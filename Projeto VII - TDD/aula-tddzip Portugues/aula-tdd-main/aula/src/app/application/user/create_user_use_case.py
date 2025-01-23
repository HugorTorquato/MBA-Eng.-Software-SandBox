
from dataclasses import dataclass
from domain.User.user_repository_interface import UserRepositoryInterface
from domain.User.user_entity import User
from uuid import uuid4, UUID

@dataclass
class CreateUserResponse:
    id: UUID
    name: str

@dataclass
class CreateUserRequest:
    name: str

class CreateUserUseCase:

    def __init__(self, repository: UserRepositoryInterface):
        self.repository = repository

    def execute(self, request: CreateUserRequest) -> CreateUserResponse:
        user = User(id=uuid4(), name=request.name)
        self.repository.save(user=user) # Essa parte vai ser simulada pelo mocker

        return CreateUserResponse(id=user.id, name=user.name)