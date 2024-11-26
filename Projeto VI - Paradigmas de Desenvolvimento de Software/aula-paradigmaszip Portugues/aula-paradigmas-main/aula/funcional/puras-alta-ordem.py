

# Funções puras
    # retorna 1 valor de dois valores
    # Não tem efeito colateral, sempre gera o mesmo resultado

def soma(a,b):
    return a+b

print(soma(2,3))

# Funções de alta ordem

    # Função que recebe e utiliza funções dentro de uma função
    # Nível de abstração maior
    # Paradigma funcional 

def aplicar_duas_vezes(func, valor):
    return func(func(valor))

def incrementar(x):
    return x + 1

print(incrementar(5))

print(aplicar_duas_vezes(incrementar, 6))
