"""Calculadora 2 - Intermedia.
Usa funciones y un menú con bucle while.
"""


def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return "Error: división por cero"
    return a / b


def main():
    while True:
        print("\n=== Calculadora ===")
        print("1) Sumar  2) Restar  3) Multiplicar  4) Dividir  5) Salir")
        opcion = input("Opción: ")

        if opcion == "5":
            print("¡Adiós!")
            break

        if opcion not in ("1", "2", "3", "4"):
            print("Opción inválida")
            continue

        try:
            a = float(input("a: "))
            b = float(input("b: "))
        except ValueError:
            print("Debes ingresar números")
            continue

        if opcion == "1":
            print("Resultado:", sumar(a, b))
        elif opcion == "2":
            print("Resultado:", restar(a, b))
        elif opcion == "3":
            print("Resultado:", multiplicar(a, b))
        else:
            print("Resultado:", dividir(a, b))


if __name__ == "__main__":
    main()
