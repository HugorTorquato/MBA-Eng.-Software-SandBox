# lib para fazer validação da classe
from pydantic import BaseModel
from typing import List
from uuid import UUID

#INPUT

# O base model vai fazer validação de tipos de entraras
class ListUserInputDTO(BaseModel):
    pass # Not defined yet in the contract

class UserDto(BaseModel):
    id:UUID
    name:str

#OUTPUT
class ListUserOutputDTO(BaseModel):
    users: List[UserDto]

