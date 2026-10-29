"""Dia 3 - Agenda mejorada (reto).
Mismos conceptos + validacion de duplicados y contador.
"""


def agregar_contacto(contactos):
    nombre = input("Nombre: ").strip()
    email = input("Email: ").strip()

    # Evita duplicados comparando nombres en minusculas
    for c in contactos:
        if c["nombre"].lower() == nombre.lower():
            print(f"'{nombre}' ya existe en la agenda.")
            return

    contacto = {
        "nombre": nombre,
        "email": email,
    }
    contactos.append(contacto)
    print(f"Contacto '{nombre}' agregado. Total: {len(contactos)}")


def listar_contactos(contactos):
    if not contactos:
        print("La agenda esta vacia.")
        return

    for i, c in enumerate(contactos, start=1):
        print(f"{i}. {c['nombre']} | {c['email']}")


def eliminar_contacto(contactos, nombre):
    for c in contactos:
        if c["nombre"].lower() == nombre.lower():
            contactos.remove(c)
            print(f"Contacto '{nombre}' eliminado. Total: {len(contactos)}")
            return
    print(f"No existe '{nombre}'.")


def main():
    contactos = []
    print("=== Agenda mejorada ===\n")

    while True:
        print("1) Agregar  2) Listar  3) Eliminar  4) Salir")
        opcion = input("Opción: ").strip()

        if opcion == "4":
            print("Adios!")
            break

        if opcion == "1":
            agregar_contacto(contactos)
        elif opcion == "2":
            listar_contactos(contactos)
        elif opcion == "3":
            nombre = input("Nombre a eliminar: ").strip()
            eliminar_contacto(contactos, nombre)
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
