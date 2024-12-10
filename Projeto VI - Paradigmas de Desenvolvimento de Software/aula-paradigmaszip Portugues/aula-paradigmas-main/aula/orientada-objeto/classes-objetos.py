

class Carro:


    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def emitir_som(self):
        print("vrumm")

    def emitir_detalhes(self):
        print(self.marca)
        print(self.modelo)
        print(self.ano)
        self.emitir_som()

# Criação de um objeto da classe Carro
carro1 = Carro(marca="Toyota", modelo="Corolla", ano=2020)
carro2 = Carro(marca="Fiat", modelo="Uno", ano=2021)

print(carro1.modelo)
print(carro2.modelo)