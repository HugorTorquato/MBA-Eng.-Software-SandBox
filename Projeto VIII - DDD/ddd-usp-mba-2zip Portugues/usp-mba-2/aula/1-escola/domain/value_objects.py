# Não colocamos um identificador, algo que podemos identificar de forma unica

# Temos de ter
# id
# nome
# email -> precisa de validação
# telefone

# O que está guiando a implementação são as regras dos slides!!!!
# Objeto de valor não tem identificação


from pydantic import BaseModel, EmailStr, validator
import re
from enum import Enum

class Periodo(Enum):
    MANHA = "manha"
    TARDE = "tarde"
    NOITE = "noite"

class StatusMatricula(Enum):
    ATIVO = "ativo"
    CONCLUIDO = "concluido"

class Email(BaseModel):
    email: EmailStr # Já faz a validação desse objecto de valor

class Telefone(BaseModel):
    numero: str

    # Caso tenha de alterar depois ou aceitar números de que seguem outra regra, basta
    # atualizar a lógica aqui
    @validator('numero')
    def validar_telefone(cls, value):
        if not re.match(r"^\d{2}-\d{4,5}-\d{4}$", value):
            raise ValueError("\formato de telefone inválido!\n O formato deve ser DDD-99999-9999")
        return value
    
class CodigoTreinamento(BaseModel):
    codigo: str

    @validator('codigo')
    def validar_codigo(cls, value):
        if not re.match(r"^[A-Z]{2}[0-9]{2}", value):
            raise ValueError("\n O código do treinamento está inválido!")
        return value
    
# Caso a base de dados tenha dados que não esteja de acordo com as validações, utilizamos um adapter para converter a informação
# para o que temos de regra aqui. e não corrompemos o que já foi implementado ( importante ter adaters !!!! )
# Uma forma de proteger o dominio principal
    