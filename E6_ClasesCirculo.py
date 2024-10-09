import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio
        self.area = self.calcular_area()

    def calcular_area(self):
        return math.pi * self.radio ** 2

# Usar la clase Circulo y mostrar los valores

# Crear un círculo con radio 5
circulo = Circulo(8)  

#Imprime resultados
print(f"Radio del círculo: {circulo.radio}")
print(f"Área del círculo: {circulo.area}")