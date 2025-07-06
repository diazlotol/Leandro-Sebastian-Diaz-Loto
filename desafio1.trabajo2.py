class Estudiante:
    def __init__(self, nombre, nota):
        self.__nombre = nombre
        self.__nota = nota

    def obtener_nombre(self):
        return self.__nombre

    def obtener_nota(self):
        return self.__nota

    def esta_aprobado(self):
        return self.__nota >= 60

# Ejemplo de uso
if __name__ == "__main__":
    nombre = input("Ingrese el nombre del estudiante: ")
    nota = float(input("Ingrese la nota del estudiante: "))

    estudiante = Estudiante(nombre, nota)

    print(f"\nNombre: {estudiante.obtener_nombre()}")
    print(f"Nota: {estudiante.obtener_nota()}")
    if estudiante.esta_aprobado():
        print("Resultado: Aprobado")
    else:
        print("Resultado: No Aprobado")
