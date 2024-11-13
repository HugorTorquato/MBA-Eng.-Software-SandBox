#Representação do metadados do banco de dados

from infrastructure.api.database import Base
from sqlalchemy import Column, String
from sqlalchemy .dialects.postgresql import UUID

class UserModel(Base):

    # de acordo com o que estamos trabalhando agora

    # Toda tabela implementada aqui vai ser definida no banco de dados
    __tablename__ = "tb_users"

    id = Column(UUID, primar_key=True, index=True)
    name = Column(String)
