class Calculadora:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def sumar(self):
        return self.numero1 + self.numero2

    def restar(self):
        return self.numero1 - self.numero2

    def multiplicar(self):
        return self.numero1 * self.numero2

    def dividir(self):
        if self.numero2 != 0:
            return self.numero1 / self.numero2
        else:
            return "Error: División por cero"

# Ejemplo de uso
if __name__ == "__main__":
    try:
        num1 = int(input("Ingrese el primer número entero: "))
        num2 = int(input("Ingrese el segundo número entero: "))

        calculadora = Calculadora(num1, num2)

        print(f"\nSuma: {calculadora.sumar()}")
        print(f"Resta: {calculadora.restar()}")
        print(f"Multiplicación: {calculadora.multiplicar()}")
        print(f"División: {calculadora.dividir()}")

    except ValueError:
        print("Error: Ingrese solo valores enteros.")
