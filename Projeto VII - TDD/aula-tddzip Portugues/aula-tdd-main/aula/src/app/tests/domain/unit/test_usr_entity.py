# Classe user encapsula os dados do usuáro

from uuid import uuid4
import pytest
from domain.User.user_entity import User

class TestUser:
    # Tudo que for teste de user vai ser encapsulado aqui dentro

    #Teste para construir o usuário
    #Cria um metodo para testar essa construção do user
    def test_user_initialization(self):
        # Agora eu sei o que preciso para implementar a classe usuário
        user_id = uuid4()
        user_name = "Hugo"

        user = User(id=user_id, name=user_name)

        assert user.id == user_id
        assert user.name == user_name

    #Teste para validação do ID do user
    def test_user_id_validation(self):
        
        # Usar a lib do pytest, para trazer exceptions para nós
            # test tem de ficar dentro do with, pq o escopo acaba depois dele

        with pytest.raises(Exception, match="id must be an UUID"):
            User(id="id_invalido", name="Hugo")

    #Teste para validação do name do user
    def test_user_name_validation(self):
        user_id = uuid4()
        # Usar a lib do pytest, para trazer exceptions para nós
            # test tem de ficar dentro do with, pq o escopo acaba depois dele

        with pytest.raises(Exception, match="name is required"):
            User(id=user_id, name="")