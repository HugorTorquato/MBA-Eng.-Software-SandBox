
# Somar números até atingr um limite

limite = 100

soma = 0

numero = 1

# enquanto a soma for menor que um limite, continua somando

while soma < limite:
    soma += numero
    numero += 1
    print(soma)
    print(numero)

print(soma)

# Encontrar primeiro número divisível por 7 no intervalo

for numero in range(1, 100):
    if numero % 7 == 0:
        print(numero)
        break

# Verificar se todos os itens de uam lista são positivos

numeros = [1,2,3,8,9]
todos_positivos = True  

for numero in numeros:
    if numero < 0:
        todos_positivos = False

print(todos_positivos)