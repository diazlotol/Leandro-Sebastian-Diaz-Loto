class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cantidad = 0

    def depositar(self, monto):
        if monto > 0:
            self.cantidad += monto
            print(f"{self.nombre} depositó ${monto}")
        else:
            print("⚠️ Monto de depósito inválido")

    def extraer(self, monto):
        if 0 < monto <= self.cantidad:
            self.cantidad -= monto
            print(f"{self.nombre} extrajo ${monto}")
        else:
            print(f"⚠️ {self.nombre} no puede extraer ${monto}. Saldo insuficiente.")

    def get_total(self):
        return self.cantidad

    def mostrar_datos(self):
        print(f"{self.nombre} tiene ${self.cantidad}")


class Banco:
    def __init__(self):
        self.cliente1 = Cliente("Ana")
        self.cliente2 = Cliente("Luis")
        self.cliente3 = Cliente("Juan")

    def operar(self):
        # Aquí puedes definir las operaciones del día
        self.cliente1.depositar(1000)
        self.cliente2.depositar(1500)
        self.cliente3.depositar(2000)

        self.cliente1.extraer(400)
        self.cliente3.extraer(1000)

    def deposito_total(self):
        total = (
            self.cliente1.get_total() +
            self.cliente2.get_total() +
            self.cliente3.get_total()
        )
        print(f"\n💰 Total depositado en el banco: ${total}")
        print("\n📋 Saldo por cliente:")
        self.cliente1.mostrar_datos()
        self.cliente2.mostrar_datos()
        self.cliente3.mostrar_datos()


# Programa principal
if __name__ == "__main__":
    banco = Banco()
    banco.operar()
    banco.deposito_total()
