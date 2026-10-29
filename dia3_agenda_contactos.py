"""Dia 3 - Agenda de contactos.
Temas: funciones con parametros y return, listas, diccionarios.
"""


def agregar_contacto(contactos):
    nombre = input("Nombre: ").strip()
    telefono = input("Telefono: ").strip()
    email = input("Email: ").strip()

    contacto = {
        "nombre": nombre,
        "telefono": telefono,
        "email": email,
    }
    contactos.append(contacto)
    print(f"Contacto '{nombre}' agregado.")


def listar_contactos(contactos):
    if not contactos:
        print("La agenda esta vacia.")
        return

    print(f"\n=== Contactos ({len(contactos)}) ===")
    for c in contactos:
        print(f"- {c['nombre']} | {c['telefono']} | {c['email']}")


def buscar_contacto(contactos, nombre):
    for c in contactos:
        if c["nombre"].lower() == nombre.lower():
            print(f"\nEncontrado: {c['nombre']} | {c['telefono']} | {c['email']}")
            return c
    print(f"No existe ningun contacto llamado '{nombre}'.")
    return None


def eliminar_contacto(contactos, nombre):
    for c in contactos:
        if c["nombre"].lower() == nombre.lower():
            contactos.remove(c)
            print(f"Contacto '{nombre}' eliminado.")
            return True
    print(f"No existe ningun contacto llamado '{nombre}'.")
    return False


def main():
    contactos = []
    print("=== Agenda de contactos ===")
    print("Escribe 'salir' en cualquier menu para terminar.\n")

    while True:
        print("\n1) Agregar  2) Listar  3) Buscar  4) Eliminar  5) Salir")
        opcion = input("Opción: ").strip()

        if opcion == "5":
            print("Adios!")
            break

        if opcion == "1":
            agregar_contacto(contactos)
        elif opcion == "2":
            listar_contactos(contactos)
        elif opcion == "3":
            nombre = input("Nombre a buscar: ").strip()
            buscar_contacto(contactos, nombre)
        elif opcion == "4":
            nombre = input("Nombre a eliminar: ").strip()
            eliminar_contacto(contactos, nombre)
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
