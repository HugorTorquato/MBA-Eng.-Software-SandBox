

# Entrada -> Função -> Saida ( propria função )

# fatorial de 4: 4 * 3 * 2 * 1

def fatorial(numero):
    # Importante a definição de um break para n cair em loop
    if numero == 0:
        return 1

    return numero * fatorial(numero - 1)        

print(fatorial(4))

def fibonacci(numero):

    if numero == 0:
        return 0
    elif numero == 1:
        return 1
    return fibonacci(numero -2) + fibonacci(numero -1)

print(fibonacci(6))