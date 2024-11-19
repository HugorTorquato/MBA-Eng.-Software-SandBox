
#Metodos que vão existir lá no repositório

# Classe abstrata que vai ter diversos outros metodos que podem ser
# implmentados para qualquer repostório ou banco de dados

# Toda classe que receber essa injeção de dependencia va ter de implementar esses metodos

from abc import ABC, abstractmethod
from domain.User.user_entity import User
from uuid import UUID
from typing import List

#User entity interface ( what we will expect to have implemented)
class UserRepositoryInterface(ABC):
    
    # Implementar a camada do contrato

    @abstractmethod
    def add_user(self, user: User) -> None:
        #Espero None como output

        #Como não temos impementação vai levantar um erro.
        # Isso garante que o que concetar nessa interface vai respeitar o contrato
        raise NotImplementedError
        
    @abstractmethod
    def find_user(self, user_id: UUID) -> User:
        raise NotImplementedError
        
    @abstractmethod
    def update_user(self, user: User) -> None:
        raise NotImplementedError
        
    @abstractmethod
    def list_user(self) -> List[User]:
        raise NotImplementedError