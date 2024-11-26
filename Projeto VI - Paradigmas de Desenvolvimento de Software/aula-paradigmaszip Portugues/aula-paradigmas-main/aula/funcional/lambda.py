
# Funções em 1 linha sem nome

# dobro = lambda <Atributos de entrada>:< saida da função>
dobro = lambda x : x * 2

print(dobro(4))

valores = [1,2,3,4]
valores_dobrados = list(map(lambda x : x * 2, valores))

print(valores_dobrados)

# Calcular números pares
numeros = [1,2,3,4,5,6,7,8,9,10]
numros_impares = []

for numero in numeros:
    if numero % 2 != 0:
        numros_impares.append(numero)

print(numros_impares)

numros_impares2 = []
numros_impares2 = list(filter(lambda x : x%2 != 0, numeros))

print(numros_impares2)