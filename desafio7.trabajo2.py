class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.set_nombre(nombre)
        self.set_edad(edad)
        self.set_dni(dni)

    # Getter y Setter para nombre
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        if isinstance(nombre, str):
            self.__nombre = nombre
        else:
            print(" Nombre inválido (debe ser texto)")
            self.__nombre = ""

    # Getter y Setter para edad
    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        if isinstance(edad, int) and 0 <= edad <= 120:
            self.__edad = edad
        else:
            print(" Edad inválida (debe ser un entero entre 0 y 120)")
            self.__edad = 0

    # Getter y Setter para DNI
    def get_dni(self):
        return self.__dni

    def set_dni(self, dni):
        if isinstance(dni, str) and dni.isdigit() and len(dni) in [7, 8]:
            self.__dni = dni
        else:
            print(" DNI inválido (debe ser numérico y tener 7 u 8 dígitos)")
            self.__dni = ""

    # Mostrar información
    def mostrar(self):
        print(" Datos de la persona:")
        print(f"Nombre: {self.get_nombre()}")
        print(f"Edad: {self.get_edad()}")
        print(f"DNI: {self.get_dni()}")

    # Verifica si es mayor de edad
    def es_mayor_de_edad(self):
        return self.get_edad() >= 18


# Ejemplo de uso
if __name__ == "__main__":
    persona1 = Persona("Juan Pérez", 25, "34567890")
    persona1.mostrar()
    print("¿Es mayor de edad?", " Sí" if persona1.es_mayor_de_edad() else "❌ No")

    print("\n--- Persona con datos inválidos ---")
    persona2 = Persona(123, -5, "abc")
    persona2.mostrar()
