
# lib para fazer validação da classe
from pydantic import BaseModel
from uuid import UUID

# Implementação do DTO, e az a verificação
# Objeto de transferencia de dado

# Ser o mais primitivo possível

#INPUT
class FindUserInputDTO(BaseModel):
    id: UUID

#OUTPUT
class FindUserOutputDTO(BaseModel):
    id: UUID
    name: str
