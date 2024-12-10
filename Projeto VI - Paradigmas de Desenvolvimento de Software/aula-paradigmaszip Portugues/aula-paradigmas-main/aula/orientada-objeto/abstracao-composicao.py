from abc import ABC, abstractmethod


############## Abstração

# Toda forma geometrica tem de calcular area, e cada classe filho vai ter de impementar essas funçoes
class FormaGeometrica(ABC): # abc define como classe abstrata

    @abstractmethod # Esse etodo é agora um abstrato
    def calcular_area(self):
        raise NotImplementedError("Este metodo deve ser implementado")
    

# Temos as heranças dos dados
class Circulo(FormaGeometrica):

    def __init__(self, raio):
        self.raio = raio

    # Obrigado implementar o etodo calcular_Area ( muito utilizado na arquitetura limpa )
    def calcular_area(self):
        return 3.14 * self.raio ** 2

circulo = Circulo(raio=10)
print(circulo.calcular_area())

# Temos as heranças dos dados
class Retangulo(FormaGeometrica):

    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    # Obrigado implementar o etodo calcular_Area ( muito utilizado na arquitetura limpa )
    def calcular_area(self):
        return self.largura * self.altura
    
retangulo = Retangulo(largura=5, altura=4)
print(retangulo.calcular_area())

################### Composção
# Compor classes diferentes com atributos de outras classes
class Motor:

    def __init__(self, potencia):
        self.potencia = potencia
        self.ligado = False

    def ligar_motor(self):
        self.ligado = True

class Carro:
    
    def __init__(self, marca, modelo, motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor

    def exibir_detalhes(self):
        print(f"Carro {self.marca} {self.modelo}")
        self.mostrar_potencia_motor()

    def mostrar_potencia_motor(self):
        print(f"Motor de potencia: {self.motor.potencia} cavalos")
        
# a classe motor é passada como atributo da classe carro
motor1 = Motor(potencia=200)
carro1 = Carro(marca="Fiat", modelo="Uno", motor=motor1)

print(carro1.exibir_detalhes())

