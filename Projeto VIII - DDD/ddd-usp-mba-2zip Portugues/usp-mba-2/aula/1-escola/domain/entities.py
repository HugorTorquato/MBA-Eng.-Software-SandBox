
#Definir as entidades que tem de crir

from pydantic import BaseModel, Field
from .value_objects import Email, Telefone, CodigoTreinamento, StatusMatricula, Periodo
from datetime import date

class Aluno(BaseModel):
    """Args: ID, nome, email, telefone"""
    id: int = Field(..., gt=0) # Validação de que o valor tem de ser maior que 0
    nome: str
    # Tenho de seguir as regras do value_objects
    email: Email
    telefone: Telefone

class Treinamento(BaseModel):
    """Args: ID, codigo, descrião, carga_horara, capacidade"""
    id: int = Field(..., gt=0)
    codigo: CodigoTreinamento
    descricao: str
    carga_horaria: int = Field(..., gt=0)
    capacidade: int = Field(..., gt=0)

# Coração da aplicação ( o que faz o dominio ter sentido ) 

class Matricula(BaseModel):
    """Args: ID, aluno, treinamento, periodo, status, data_inicio"""
    id: int = Field(..., gt=0)
    aluno: Aluno
    treinamento: Treinamento
    periodo: Periodo
    status: StatusMatricula = StatusMatricula.ATIVO
    data_inicio: date

