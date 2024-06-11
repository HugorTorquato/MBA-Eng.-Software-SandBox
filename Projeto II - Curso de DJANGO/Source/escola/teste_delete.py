import requests

headers = {'Authorization': 'Token 6d784678d890946237dcc1bbe2396ff7bd8a4940'}
url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'

#curso = requests.get(url=f'{url_base_cursos}3/', headers=headers)
#print(curso.json())

resultado = requests.delete(url=f'{url_base_cursos}3/', headers=headers)
assert resultado.status_code == 204
assert len(resultado.text) == 0