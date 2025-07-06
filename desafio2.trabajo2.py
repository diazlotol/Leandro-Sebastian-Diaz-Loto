class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def lado_mayor(self):
        return max(self.lado1, self.lado2, self.lado3)

    def tipo_triangulo(self):
        if self.lado1 == self.lado2 == self.lado3:
            return "Equilátero"
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            return "Isósceles"
        else:
            return "Escaleno"

# Ejemplo de uso
if __name__ == "__main__":
    l1 = float(input("Ingrese el primer lado del triángulo: "))
    l2 = float(input("Ingrese el segundo lado del triángulo: "))
    l3 = float(input("Ingrese el tercer lado del triángulo: "))

    # Validar si forma un triángulo
    if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
        triangulo = Triangulo(l1, l2, l3)
        print(f"\nLado mayor: {triangulo.lado_mayor()}")
        print(f"Tipo de triángulo: {triangulo.tipo_triangulo()}")
    else:
        print("Los lados ingresados no forman un triángulo válido.")
