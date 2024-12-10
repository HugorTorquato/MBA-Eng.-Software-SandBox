

# manter coisas expostas ou não dentro de uma classe

class ContaBancaria:

    def __init__(self, titular, saldo_inicial = 0):
        self.titular = titular
        self.__saldo_inicial = saldo_inicial # Essa propriedade é privada na classe

    def get_saldo(self):
        return self.__saldo_inicial
    
    def depositar_Valor(self, valor):
        if valor > 0:
            self.__saldo_inicial += valor
        else:
            print("valor tem de ser maior que zero")

    def retirar_valor(self, valor):
        if self.__saldo_inicial < valor:
            self.__saldo_inicial -= valor
        else:
            print("Saldo insuficiente")
        

conta_a = ContaBancaria(titular="Maria", saldo_inicial=200)
conta_b = ContaBancaria(titular="Hugo", saldo_inicial=40000)

print(conta_a.titular)
# print(conta_a.__saldo_inicial)
print(conta_a.get_saldo())

conta_a.depositar_Valor(100)
conta_a.retirar_valor(300)

