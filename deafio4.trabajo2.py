class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return f"Nombre: {self.nombre}, Teléfono: {self.telefono}, Email: {self.email}"

class Agenda:
    def __init__(self):
        self.contactos = []

    def crear_contacto(self):
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        email = input("Email: ")
        self.contactos.append(Contacto(nombre, telefono, email))
        print("✅ Contacto creado exitosamente.")

    def borrar_contacto(self):
        nombre = input("Ingrese el nombre del contacto a borrar: ")
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                self.contactos.remove(contacto)
                print("🗑️ Contacto borrado exitosamente.")
                return
        print("⚠️ Contacto no encontrado.")

    def editar_contacto(self):
        nombre = input("Ingrese el nombre del contacto a editar: ")
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                nuevo_nombre = input("Nuevo nombre (enter para mantener): ")
                nuevo_telefono = input("Nuevo teléfono (enter para mantener): ")
                nuevo_email = input("Nuevo email (enter para mantener): ")

                if nuevo_nombre:
                    contacto.nombre = nuevo_nombre
                if nuevo_telefono:
                    contacto.telefono = nuevo_telefono
                if nuevo_email:
                    contacto.email = nuevo_email

                print("✏️ Contacto actualizado correctamente.")
                return
        print("⚠️ Contacto no encontrado.")

    def listar_contactos(self):
        if not self.contactos:
            print("📭 La agenda está vacía.")
        else:
            print("📒 Lista de contactos:")
            for contacto in self.contactos:
                print(contacto)

    def buscar_contacto(self):
        nombre = input("Ingrese el nombre a buscar: ")
        encontrados = [c for c in self.contactos if nombre.lower() in c.nombre.lower()]
        if encontrados:
            print("🔍 Contactos encontrados:")
            for c in encontrados:
                print(c)
        else:
            print("⚠️ No se encontraron contactos con ese nombre.")

def mostrar_menu():
    print("\n===== MENÚ DE LA AGENDA =====")
    print("1. Crear contacto")
    print("2. Borrar contacto")
    print("3. Editar contacto")
    print("4. Lista de contactos")
    print("5. Buscar contacto")
    print("6. Cerrar agenda")

# Programa principal
if __name__ == "__main__":
    agenda = Agenda()
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-6): ")
        if opcion == "1":
            agenda.crear_contacto()
        elif opcion == "2":
            agenda.borrar_contacto()
        elif opcion == "3":
            agenda.editar_contacto()
        elif opcion == "4":
            agenda.listar_contactos()
        elif opcion == "5":
            agenda.buscar_contacto()
        elif opcion == "6":
            print("👋 Agenda cerrada.")
            break
        else:
            print("❌ Opción inválida. Intente de nuevo.")
