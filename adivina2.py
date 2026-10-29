
import random


def jugar(max_intentos):
    numero_secreto = random.randint(1, 100)
    intentos = 0

    print("\nAdivina el número entre 1 y 100")
    print("Tienes", max_intentos, "intentos.")

    while intentos < max_intentos:

        try:
            numero_jugador = int(input("\nIngresa un número: "))

        except ValueError:
            print("Error: debes ingresar un número entero.")
            continue

        if numero_jugador < 1 or numero_jugador > 100:
            print("El número debe estar entre 1 y 100.")
            continue

        intentos += 1

        if numero_jugador == numero_secreto:
            print("¡Felicidades! Adivinaste.")
            break

        elif numero_jugador < numero_secreto:
            print("El número secreto es mayor.")

        else:
            print("El número secreto es menor.")

        print("Intentos restantes:", max_intentos - intentos)

    else:
        print("¡Perdiste!")
        print("El número secreto era:", numero_secreto)

    print("Intentos utilizados:", intentos)


def main():
    print("Bienvenido al juego de adivinanzas")

    while True:
        print("\nSelecciona la dificultad:")
        print("1. Fácil (10 intentos)")
        print("2. Medio (7 intentos)")
        print("3. Difícil (5 intentos)")

        opcion = input("Selecciona 1, 2 o 3: ")

        if opcion == "1":
            jugar(10)

        elif opcion == "2":
            jugar(7)

        elif opcion == "3":
            jugar(5)

        else:
            print("Opción incorrecta.")
            continue

        respuesta = input("\n¿Quieres jugar otra vez? (s/n): ")

        if respuesta.lower() == "n":
            print("Gracias por jugar.")
            break


if __name__ == "__main__":
    main()
