import requests

headers = {'Authorization': 'Token 6d784678d890946237dcc1bbe2396ff7bd8a4940'}
url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'

curso_atualizado = {
    "titulo": "Novo3 curso",
    "url": "http://novocurso3.com"
}

#curso = requests.get(url=f'{url_base_cursos}3/', headers=headers)
#print(curso.json())

resultado = requests.put(url=f'{url_base_cursos}3/', headers=headers, data=curso_atualizado) #Curso id 3
assert resultado.status_code == 200
assert resultado.json()['titulo'] == curso_atualizado['titulo']
print(resultado.json())