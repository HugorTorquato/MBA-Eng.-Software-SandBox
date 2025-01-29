from domain.entities import Aluno, Treinamento
from domain.value_objects import Email, Telefone, CodigoTreinamento, Periodo
from domain.services import MatriculaService
from datetime import date


from infrastructure.cursos_xml_adapter import CursosXMLAdapter # Importar após ajustar o path


""" 
Criar instâncias de Aluno
"""
aluno1 = Aluno(id=1, nome="João Silva", email=Email(email="joao.silva@example.com"), telefone=Telefone(numero="11-99999-8888"))
aluno2 = Aluno(id=2, nome="Ana Rosa", email=Email(email="ana.rosa@example.com"), telefone=Telefone(numero="11-99999-7777")) 
aluno3 = Aluno(id=3, nome="Maria Vitória", email=Email(email="maria.vi@example.com"), telefone=Telefone(numero="11-88888-1234")) 
print('\nAlunos criados')


""" 
Criar instâncias de Treinamentos
"""
treinamento1 = Treinamento(id=1, codigo=CodigoTreinamento(codigo="PY10"), descricao="Introdução a Python", carga_horaria=40, capacidade=2)
treinamento2 = Treinamento(id=2, codigo=CodigoTreinamento(codigo="JA10"), descricao="Introdução a Python", carga_horaria=16, capacidade=10)
print('Treinamentos criados')


""" 
Criar instâncias de service para adicionar um curso e um aluno
"""
service = MatriculaService()
service.adicionar_aluno(aluno1)
service.adicionar_aluno(aluno2)
service.adicionar_aluno(aluno3)
service.adicionar_treinamento(treinamento1)


""" 
Criar matrícula de um aluno
"""
matricula1 = service.matricular_aluno(aluno1, treinamento1, Periodo.NOITE, date(2024, 3, 10))
matricula2 = service.matricular_aluno(aluno2, treinamento1, Periodo.NOITE, date(2024, 3, 11))
print('Matrículas criadas com sucesso!\n')
# matricula3 = service.matricular_aluno(aluno3, treinamento1, Periodo.TARDE, date(2024, 3, 12))

# melhorando a exibição

# try:
#     matricula3 = service.matricular_aluno(aluno3, treinamento1, Periodo.TARDE, date(2024, 3, 12))
#     print("Matrícula 3 criada:", matricula3) #não deve ser executado
# except ValueError as e:
#     print(f"Erro ao criar Matrícula 3: {e}")


"""
Testar a validação de código de treinamento inválido
"""
# try:
#     treinamento_invalido = Treinamento(id=2, codigo=CodigoTreinamento(codigo="PY101_INVALIDO"), descricao="Curso Inválido", carga_horaria=20, capacidade=5)
#     service.adicionar_treinamento(treinamento_invalido)
# except ValueError as e:
#     print(f"Erro de validação: {e}")    

"""
Matricular novamente no mesmo treinamento
"""
# try:
#     matricula2 = service.matricular_aluno(aluno1, treinamento1, Periodo.NOITE, date(2024,3,10))
#     print(matricula2)
# except ValueError as e:
#     print(f"Erro: {e}")

"""
Cadastrar um treinamento com o mesmo código
"""
# try:
#     treinamento2 = Treinamento(id=3, codigo=CodigoTreinamento(codigo="PY10"), descricao="Outro treinamento python", carga_horaria=30, capacidade=2)
#     service.adicionar_treinamento(treinamento2)
# except ValueError as e:
#     print(f"Erro: {e}")


"""
Camada anti corrupção
"""
# adapter = CursosXMLAdapter("cursos.xml")
# treinamentos = adapter.obter_treinamentos()

# print('XML')
# for treinamento in treinamentos:
#     print(f"ID: {treinamento.id}, Código: {treinamento.codigo.codigo}, Descrição: {treinamento.descricao}")
