"""Dia 2 - Ejercicio 3: Juego con menu.
Combina: while externo, funciones, condicionales.
"""

import random


def adivina_numero():
    numero_secreto = random.randint(1, 50)
    intentos = 0

    while True:
        intentos += 1
        entrada = input("Tu numero: ").strip()

        try:
            intento = int(entrada)
        except ValueError:
            print("Eso no es un numero entero.")
            intentos -= 1
            continue

        if intento < numero_secreto:
            print("Muy bajo, sube!")
        elif intento > numero_secreto:
            print("Muy alto, baja!")
        else:
            print(f"Correcto! Lo adivinaste en {intentos} intentos.")
            return intentos


def tabla_multiplicar():
    entrada = input("¿De qué numero? ").strip()

    try:
        numero = int(entrada)
    except ValueError:
        print("Eso no es un numero entero.")
        return None

    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
    return None


def main():
    while True:
        print("\n=== Menu de juegos ===")
        print("1) Adivina el numero")
        print("2) Tabla de multiplicar")
        print("3) Salir")

        opcion = input("Opción: ").strip()

        if opcion == "1":
            adivina_numero()
        elif opcion == "2":
            tabla_multiplicar()
        elif opcion == "3":
            print("¡Adiós!")
            break
        else:
            print("Opción inválida, elige 1, 2 o 3.")


if __name__ == "__main__":
    main()
