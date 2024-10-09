class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)
    
    mi_rectangulo = Rectangulo(5, 3)  # Crear un rectángulo con base 5 y altura 3
    area = mi_rectangulo.calcular_area()
    perimetro = mi_rectangulo.calcular_perimetro()

    print(f"El área del rectángulo es: {area}")        # Output: El área del rectángulo es: 15
    print(f"El perímetro del rectángulo es: {perimetro}")  # Output: El perímetro del rectángulo es: 16