class Rectangulo:
    def __init__(self, base, altura):
        if base > 0 and altura > 0:
            self.base = base
            self.altura = altura
        else:
            raise ValueError(" La base y la altura deben ser números positivos")

    def calcular_area(self):
        return self.base * self.altura

# Ejemplo de uso
if __name__ == "__main__":
    try:
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))

        rect = Rectangulo(base, altura)
        print(f" El área del rectángulo es: {rect.calcular_area()}")

    except ValueError as e:
        print(e)
