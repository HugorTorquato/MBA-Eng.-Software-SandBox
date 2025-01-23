
from domain.User.user_repository_interface import UserRepositoryInterface
from domain.User.user_entity import User

# vai gerdar o contrato para os metodos que tem de ser implementados
class InMemoryUserRepository(UserRepositoryInterface):

    def __init__(self):
        self.users: list[User] = []

    def save(self, user: User) -> None:
        self.users.append(user)

    def get_by_id(self, userId):
        
        for user in self.users:
            if user.id == userId:
                return user

        return None
    
    def update_name_by_id(self, userId, newName):
        for user in self.users:
            if user.id == userId:
                user.name = newName