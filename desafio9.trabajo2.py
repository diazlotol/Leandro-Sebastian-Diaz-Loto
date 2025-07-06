import math

class Circulo:
    def __init__(self, radio):
        if radio > 0:
            self.radio = radio
        else:
            raise ValueError(" El radio debe ser un número positivo")

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio


# Ejemplo de uso
if __name__ == "__main__":
    try:
        radio = float(input("Ingrese el radio del círculo: "))
        circulo = Circulo(radio)

        print(f" Área del círculo: {circulo.calcular_area():.2f}")
        print(f" Perímetro del círculo: {circulo.calcular_perimetro():.2f}")

    except ValueError as e:
        print(e)
