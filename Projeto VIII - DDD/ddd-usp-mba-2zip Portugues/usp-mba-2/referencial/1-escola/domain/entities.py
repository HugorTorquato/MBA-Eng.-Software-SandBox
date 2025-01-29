from .value_objects import Email, Telefone, CodigoTreinamento, Periodo, StatusMatricula
from typing import Optional
from datetime import date
from pydantic import BaseModel, validator, Field


class Aluno(BaseModel):
    id: int = Field(..., gt=0) #validação do id para ser maior que zero
    nome: str
    email: Email
    telefone: Telefone

class Treinamento(BaseModel):
    id: int = Field(..., gt=0)
    codigo: CodigoTreinamento
    descricao: str
    carga_horaria: int = Field(..., gt=0) 
    capacidade: int = Field(..., gt=0) 

class Matricula(BaseModel):
    id: int = Field(..., gt=0)
    aluno: Aluno
    treinamento: Treinamento
    periodo: Periodo
    status: StatusMatricula = StatusMatricula.ATIVO
    data_inicio: date