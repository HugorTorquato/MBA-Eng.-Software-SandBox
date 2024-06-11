import requests

headers = {'Authorization': 'Token 6d784678d890946237dcc1bbe2396ff7bd8a4940'} #6a192de3bb41380ba44d477ecce73d377ebfba1a
url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'

novo_curso = {
    "titulo": "testeUBsocial02",
    "url": "http://testeUBsocial02.com"
}

resultado = requests.post(url=url_base_cursos, headers=headers, data=novo_curso)
assert resultado.status_code == 201 #Se houve código 201 na Response
assert resultado.json()['titulo'] == novo_curso['titulo'] #Se Response retornará com mesmo informado para criar