class Vehiculo:
    def __init__(self, tipo):
        self.tipo = tipo

    def descripcion(self):
        return f"Soy un vehículo tipo: {self.tipo}"


class VehiculoTerrestre(Vehiculo):
    def __init__(self, tipo):
        super().__init__(tipo)


class Coche(VehiculoTerrestre):
    def __init__(self, modelo, color):
        super().__init__('Terrestre')
        self.modelo = modelo
        self.color = color

    def descripcion(self):
        return f"Soy un coche modelo {self.modelo} de color {self.color}"


class Bicicleta(VehiculoTerrestre):
    def __init__(self, tipo_bici):
        super().__init__('Terrestre')
        self.tipo_bici = tipo_bici

    def descripcion(self):
        return f"Soy una bicicleta tipo {self.tipo_bici}"


class Barco(Vehiculo):
    def __init__(self, tipo_barco):
        super().__init__('Acuático')
        self.tipo_barco = tipo_barco

    def descripcion(self):
        return f"Soy un barco tipo {self.tipo_barco}"
