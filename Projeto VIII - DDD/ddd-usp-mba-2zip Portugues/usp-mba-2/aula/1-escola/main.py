print('Iniciando com DDD')



from domain.entities import Aluno, Treinamento
from domain.value_objects import *
from domain.services import *
from datetime import date

"""
Criar instancias de alunos
"""

aluno1 = Aluno(id=1, nome="Hugo1", email=Email(email="hugo.1601@gmail.com"), telefone=Telefone(numero="31-91111-1111"))
aluno2 = Aluno(id=2, nome="Hugo2", email=Email(email="hugo.1601@gmail.com"), telefone=Telefone(numero="31-1111-1111"))
aluno3 = Aluno(id=3, nome="Hugo3", email=Email(email="hugo.1601@gmail.com"), telefone=Telefone(numero="31-91111-1111"))
# aluno3 = Aluno(id=3, nome="Hugo3", email=Email(email="hugo.1601@gmail.com"), telefone=Telefone(numero="31-91111-1111"))


print("Alunos criados")

"""
Criar instancias de treinamentos
"""

treinamento1 = Treinamento(id=1, codigo=CodigoTreinamento(codigo="IA01"), descricao="Curso 1", carga_horaria=40, capacidade=2)
treinamento2 = Treinamento(id=2, codigo=CodigoTreinamento(codigo="IA02"), descricao="Curso 2", carga_horaria=40, capacidade=2)
treinamento3 = Treinamento(id=3, codigo=CodigoTreinamento(codigo="IA03"), descricao="Curso 3", carga_horaria=40, capacidade=2)
# treinamento3 = Treinamento(id=3, codigo=CodigoTreinamento(codigo="IA03"), descricao="Curso 3", carga_horaria=40, capacidade=2)

print("Treinamentos criados")

"""
Criar services para registrar alunos e treinamentos
"""

service = MatriculaService()

service.adicionar_aluno(aluno1)
service.adicionar_aluno(aluno2)
service.adicionar_aluno(aluno3)

service.adicionar_treinamentos(treinamento1)
service.adicionar_treinamentos(treinamento2)
service.adicionar_treinamentos(treinamento3)

print("services criados")


"""
Matricular alunos em treinamentos
"""
matrcula1 = service.matricular_aluno(aluno=aluno1, treinamento=treinamento1, periodo=Periodo.NOITE, data_inicio=date(2025,6,10))
matrcula2 = service.matricular_aluno(aluno=aluno2, treinamento=treinamento1, periodo=Periodo.NOITE, data_inicio=date(2025,6,10))
# matrcula3 = service.matricular_aluno(aluno=aluno3, treinamento=treinamento1, periodo=Periodo.NOITE, data_inicio=date(2025,6,10))

print("Matricular alunos em treinamentos criados")

