# Dizer quais metodos o repositório tem de implementar

from abc import ABC, abstractmethod
from uuid import uuid4

from domain.User.user_entity import User

# Criação de uma classe abstrata para ditar como que deve ser feita a implementação
# da integração com o banco de dados

# Nesse caso vamos usar um reposirório em memoria, mas temos também que um sql da vida
# tem de seguir os memos padrões e fica uma estrutura plug and play

class UserRepositoryInterface(ABC):

    @abstractmethod
    def save(self, user: User) -> None:
        # Se esse metodo não for implementado, essa exception vai aparecer
        raise NotImplemented
    
    @abstractmethod
    def get_by_id(self, userId: uuid4) -> User:
        return NotImplemented
    
    @abstractmethod
    def update_name_by_id(self, userId: uuid4, newName: str) -> None:
        return NotImplemented
    
