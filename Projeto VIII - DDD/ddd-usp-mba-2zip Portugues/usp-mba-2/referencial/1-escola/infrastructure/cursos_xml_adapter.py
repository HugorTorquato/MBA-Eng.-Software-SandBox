import xml.etree.ElementTree as ET
from typing import List

from domain.entities import Treinamento
from domain.value_objects import CodigoTreinamento


class CursoLegado:
    def __init__(self, id: int, codigo: str, descricao: str, carga_horaria: int, capacidade: int):
        self.id = id
        self.codigo = codigo
        self.descricao = descricao
        self.carga_horaria = carga_horaria
        self.capacidade = capacidade


class CursosXMLAdapter:
    def __init__(self, xml_path: str):
        self.xml_path = xml_path

    def obter_treinamentos(self) -> List[Treinamento]:
        tree = ET.parse(self.xml_path)
        root = tree.getroot()
        treinamentos = []

        for curso_element in root.findall('curso'):
              try:
                  treinamento = self._converter_curso_para_treinamento(curso_element)
                  treinamentos.append(treinamento)
              except ValueError as e:
                  print(f"Erro ao converter curso: {e}. Ignorando curso.")  # Log ou tratamento de erro mais robusto

        return treinamentos

    def _converter_curso_para_treinamento(self, curso_element) -> Treinamento:
        id = int(curso_element.find('id').text)
        #Adaptando o código para o formato do domínio
        codigo_bruto = curso_element.find('codigo').text

        if len(codigo_bruto) > 4:
          codigo_adaptado = codigo_bruto[:2] + str(99) 
        else:
          codigo_adaptado = codigo_bruto

        codigo = CodigoTreinamento(codigo=codigo_adaptado)  
        descricao = curso_element.find('descricao').text
        carga_horaria = int(curso_element.find('cargaHoraria').text)
        capacidade = int(curso_element.find('capacidade').text)

        return Treinamento(id=id, codigo=codigo, descricao=descricao, carga_horaria=carga_horaria, capacidade=capacidade)