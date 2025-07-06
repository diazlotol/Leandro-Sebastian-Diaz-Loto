class Persona:
    def __init__(self, nombre, apellido, dni, edad, genero):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.edad = edad
        self.genero = genero.upper()

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"


class Familia:
    def __init__(self, madre, padre, hijos):
        self.madre = madre
        self.padre = padre
        self.hijos = hijos

    def es_mayor(self, persona):
        return persona.edad >= 18

    def tiene_hijos_mayores(self):
        return any(self.es_mayor(hijo) for hijo in self.hijos)

    def tiene_hijos_menores(self):
        return any(not self.es_mayor(hijo) for hijo in self.hijos)

    def todos_hijos_mayores(self):
        return all(self.es_mayor(hijo) for hijo in self.hijos)

    def cantidad_hijos(self):
        return len(self.hijos)

    def cantidad_hijas(self):
        return sum(1 for hijo in self.hijos if hijo.genero == 'F')

    def cantidad_hijos_varones(self):
        return sum(1 for hijo in self.hijos if hijo.genero == 'M')

    def agregar_hijo(self, nuevo_hijo):
        self.hijos.append(nuevo_hijo)

    def madre_es_mayor(self):
        return self.es_mayor(self.madre)

    def padre_es_mayor(self):
        return self.es_mayor(self.padre)


class FamiliaA:
    def ejecutar(self):
        familia = self.cargar_familia()
        self.agregar_mas_hijos(familia)
        self.imprimir(familia)

    def cargar_persona(self, rol):
        print(f"\nIngrese los datos de la {rol}:")
        nombre = input("Nombre: ").strip()
        apellido = input("Apellido: ").strip()
        dni = input("DNI: ").strip()
        edad = int(input("Edad: "))
        genero = input("Género (M/F): ").strip().upper()
        return Persona(nombre, apellido, dni, edad, genero)

    def cargar_familia(self):
        madre = self.cargar_persona("madre")
        padre = self.cargar_persona("padre")

        hijos = []
        cantidad = int(input("\n¿Cuántos hijos/as desea ingresar?: "))
        for i in range(cantidad):
            print(f"\nIngrese los datos del hijo/a {i + 1}:")
            hijo = self.cargar_persona("hijo/a")
            hijos.append(hijo)

        return Familia(madre, padre, hijos)

    def agregar_mas_hijos(self, familia):
        while True:
            respuesta = input("\n¿Desea agregar un nuevo hijo/a? (s/n): ").strip().lower()
            if respuesta == 's':
                nuevo_hijo = self.cargar_persona("nuevo hijo/a")
                familia.agregar_hijo(nuevo_hijo)
                print("Nuevo hijo/a agregado correctamente.")
            elif respuesta == 'n':
                break
            else:
                print("Respuesta no válida. Escriba 's' o 'n'.")

    def imprimir(self, familia):
        print("\n----- INFORME DE LA FAMILIA -----\n")

        print(f"Madre: {familia.madre.nombre_completo()}")
        print(f"Padre: {familia.padre.nombre_completo()}")

        print(f"\n¿La madre es mayor de edad? {'Sí' if familia.madre_es_mayor() else 'No'}")
        print(f"¿El padre es mayor de edad? {'Sí' if familia.padre_es_mayor() else 'No'}")

        print("\nHijos:")
        for hijo in familia.hijos:
            genero = "Mujer" if hijo.genero == "F" else "Varón"
            mayor = "mayor" if familia.es_mayor(hijo) else "menor"
            print(f" - {hijo.nombre_completo()} ({genero}, {mayor} de edad)")

        print(f"\n¿Tiene hijos mayores? {'Sí' if familia.tiene_hijos_mayores() else 'No'}")
        print(f"¿Tiene hijos menores? {'Sí' if familia.tiene_hijos_menores() else 'No'}")
        print(f"¿Todos los hijos son mayores? {'Sí' if familia.todos_hijos_mayores() else 'No'}")
        print(f"Cantidad de hijos: {familia.cantidad_hijos()}")
        print(f"Cantidad de hijas: {familia.cantidad_hijas()}")
        print(f"Cantidad de hijos varones: {familia.cantidad_hijos_varones()}")


# Ejecutar la aplicación
if __name__ == "__main__":
    app = FamiliaA()
    app.ejecutar()
