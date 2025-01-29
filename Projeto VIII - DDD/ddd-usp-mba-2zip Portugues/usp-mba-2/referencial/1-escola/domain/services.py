from .entities import Aluno, Treinamento, Matricula
from .value_objects import Periodo, StatusMatricula
from typing import List, Dict
from datetime import date


class MatriculaService:  #Servico de dominio - sem dependencia de repositorio
  def __init__(self):
      self.matriculas: Dict[int, Matricula] = {} #Simulando um repositorio em memoria
      self.proximo_id_matricula = 1
      self.alunos: Dict[int, Aluno] = {}  # Simulando um repositório em memória
      self.treinamentos: Dict[int, Treinamento] = {} #Simulando um repositorio em memoria

  def matricular_aluno(self, aluno: Aluno, treinamento: Treinamento, periodo: Periodo, data_inicio: date) -> Matricula:

        if self._aluno_possui_matricula_ativa(aluno):
            raise ValueError("Aluno já possui matrícula ativa.")

        if not self._treinamento_possui_vagas(treinamento):
            raise ValueError(f"Treinamento '{treinamento.descricao}' não possui vagas disponíveis.")

        matricula = Matricula(
            id=self.proximo_id_matricula,
            aluno=aluno,
            treinamento=treinamento,
            periodo=periodo,
            status=StatusMatricula.ATIVO,
            data_inicio=data_inicio,
        )

        self.matriculas[matricula.id] = matricula #Simulando salvar no repositorio
        self.proximo_id_matricula += 1

        return matricula

  def _aluno_possui_matricula_ativa(self, aluno: Aluno) -> bool:
        for matricula in self.matriculas.values():
            if matricula.aluno.id == aluno.id and matricula.status == StatusMatricula.ATIVO:
                return True
        return False

  def _treinamento_possui_vagas(self, treinamento: Treinamento) -> bool:
       matriculas_ativas = [
           matricula for matricula in self.matriculas.values() if matricula.treinamento.id == treinamento.id and matricula.status == StatusMatricula.ATIVO
       ]
       return len(matriculas_ativas) < treinamento.capacidade

  def adicionar_aluno(self, aluno: Aluno):
        if aluno.id in self.alunos:
            raise ValueError(f"Aluno com ID {aluno.id} já existe.")
        self.alunos[aluno.id] = aluno

  def adicionar_treinamento(self, treinamento: Treinamento):
        if treinamento.id in self.treinamentos:
            raise ValueError(f"Treinamento com ID {treinamento.id} já existe.")

        if treinamento.codigo in [t.codigo for t in self.treinamentos.values()]:
            raise ValueError(f"Já existe um treinamento com o código {treinamento.codigo}.")    

        self.treinamentos[treinamento.id] = treinamento