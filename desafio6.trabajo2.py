class Cuenta:
    def __init__(self, titular, cantidad, tipo_cuenta):
        self.titular = titular
        self.cantidad = cantidad
        self.tipo_cuenta = tipo_cuenta

    def consultar_datos(self):
        print(f"Titular: {self.titular}")
        print(f"Cantidad: ${self.cantidad}")
        print(f"Tipo de cuenta: {self.tipo_cuenta}")


class CajaAhorro(Cuenta):
    def __init__(self, titular, cantidad):
        super().__init__(titular, cantidad, "Caja de Ahorro")

    def consultar_tipo_cuenta(self):
        print(f"{self.titular} tiene una {self.tipo_cuenta}")


class PlazoFijo(Cuenta):
    def __init__(self, titular, cantidad, plazo, interes):
        super().__init__(titular, cantidad, "Plazo Fijo")
        self.plazo = plazo  # en días
        self.interes = interes  # porcentaje

    def obtener_importe_interes(self):
        return self.cantidad * self.interes / 100

    def consultar_datos_completos(self):
        self.consultar_datos()
        print(f"Plazo: {self.plazo} días")
        print(f"Interés: {self.interes}%")
        print(f"Interés generado: ${self.obtener_importe_interes():.2f}")


# Instanciar objetos de cada subclase
if __name__ == "__main__":
    # Caja de ahorro
    cliente1 = CajaAhorro("Ana Pérez", 1500)
    cliente2 = CajaAhorro("Luis Gómez", 2500)

    print("📁 Cuentas Caja de Ahorro:")
    cliente1.consultar_datos()
    cliente1.consultar_tipo_cuenta()
    print()
    cliente2.consultar_datos()
    cliente2.consultar_tipo_cuenta()

    # Plazo fijo
    print("\n📁 Cuentas Plazo Fijo:")
    cliente3 = PlazoFijo("María Torres", 5000, plazo=30, interes=2.5)
    cliente4 = PlazoFijo("Carlos Díaz", 10000, plazo=60, interes=3.0)

    cliente3.consultar_datos_completos()
    print()
    cliente4.consultar_datos_completos()
