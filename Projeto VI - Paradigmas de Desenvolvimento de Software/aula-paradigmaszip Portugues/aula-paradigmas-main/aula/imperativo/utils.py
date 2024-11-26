def calcula_media(notas):
    soma = 0
    quantidade = 0
    for nota in notas:
        soma+=nota
        quantidade += 1
    return soma/quantidade