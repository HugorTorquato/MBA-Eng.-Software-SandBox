# lib para fazer validação da classe
from pydantic import BaseModel
from uuid import UUID


# 


#INPUT
class UpdateUserInputDTO(BaseModel):
    id:UUID
    name:str

#OUTPUT
class UpdateUserOutputDTO(BaseModel):
    id:UUID
    name:str
