"""Dia 2 - Ejercicio 1: Adivina el numero.
Temas: bucle while, condicionales, modulo random.
"""

import random


def main():
    numero_secreto = random.randint(1, 100)
    intentos = 0

    print("=== Adivina el numero (1-100) ===")
    print("Tienes intentos ilimitados, pero intenta en pocos!\n")

    while True:
        intentos += 1
        entrada = input("Tu numero: ").strip()

        try:
            intento = int(entrada)
        except ValueError:
            print("Eso no es un numero entero. Intenta de nuevo.")
            intentos -= 1
            continue

        if intento < numero_secreto:
            print("Muy bajo, sube!")
        elif intento > numero_secreto:
            print("Muy alto, baja!")
        else:
            print(f"\nCorrecto! Lo adivinaste en {intentos} intentos.")
            break


if __name__ == "__main__":
    main()
