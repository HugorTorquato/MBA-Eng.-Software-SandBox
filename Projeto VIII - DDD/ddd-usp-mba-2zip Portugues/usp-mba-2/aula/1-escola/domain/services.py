# Principal atividade são as ações para os dominios



# Atendente tem de conseguir matricular o aluno de acordo com agumas regras

from .entities import *
from .value_objects import *

from typing import Dict
from datetime import date

class MatriculaService:
    
    def __init__(self):
        self.matriculas: Dict[int, Matricula] = {}
        self.alunos: Dict[int, Aluno] = {}
        self.treinamentos: Dict[int, Treinamento] = {}
        self.proximo_id_matricula = 1

    def matricular_aluno(self, aluno: Aluno, treinamento: Treinamento,
                          periodo: Periodo, data_inicio: date) -> Matricula:
        
        if self._possui_matricula_ativa(aluno):
            raise ValueError(f"Aluno {aluno.nome} possui matricula ativa!!")
        
        if not self._treinamento_possui_vagas(treinamento):
            raise ValueError(f"Esse treinamento {treinamento} está lotado")
        
        matricula = Matricula(
            id = self.proximo_id_matricula,
            aluno = aluno,
            treinamento = treinamento,
            periodo = periodo,
            data_inicio = data_inicio
        )

        self.matriculas[matricula.id] = matricula
        self.proximo_id_matricula += 1

        return matricula
    
    def adicionar_aluno(self, aluno: Aluno):
        if aluno.id in self.alunos:
            raise ValueError(f"O aluno com ID{aluno.id} já está cadastrado!")
        self.alunos[aluno.id] = aluno

    def adicionar_treinamentos(self, treinamento: Treinamento):
        # Não pode ter 2 códigos iguais e 2 ids iguais
        if treinamento.id in self.treinamentos:
            raise ValueError(f"O treinamento com ID{treinamento.ID} já está cadastrado!")
        
        if treinamento.codigo in [t.codigo for t in self.treinamentos.values()]:
            raise ValueError(f"Já existe um treinamento com o código {treinamento.codigo}.")   
        
        self.treinamentos[treinamento.id] = treinamento
        
    def _possui_matricula_ativa(self, aluno: Aluno) -> bool:
        for matricula in self.matriculas.values():
            if matricula.aluno.id == aluno.id and matricula.status == StatusMatricula.ATIVO:
                return True
        return False    
        
    def _treinamento_possui_vagas(self, treinamento: Treinamento) -> bool:
        count = 0
        for matricula in self.matriculas.values():
            if matricula.treinamento.codigo == treinamento.codigo:
                count +=1
        if count >= treinamento.capacidade:
            return False
        return True