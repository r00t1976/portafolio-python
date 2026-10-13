"""Dia 2 - Ejercicio 2: Tabla de multiplicar.
Temas: bucle for, range, f-strings.
"""


def main():
    entrada = input("¿De qué numero quieres la tabla? ").strip()

    try:
        numero = int(entrada)
    except ValueError:
        print("Eso no es un numero entero.")
        return

    print(f"\n=== Tabla del {numero} ===")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")


if __name__ == "__main__":
    main()
