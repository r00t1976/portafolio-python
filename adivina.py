
import random


def jugar():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    max_intentos = 5

    print("\nAdivina el número entre 1 y 100")
    print("Tienes 5 intentos.")

    while intentos < max_intentos:

        try:
            numero_jugador = int(input("Ingresa un número: "))

        except ValueError:
            print("Error: ingresa un número entero.")
            continue

        if numero_jugador < 1 or numero_jugador > 100:
            print("Debes ingresar un número entre 1 y 100.")
            continue

        intentos += 1

        if numero_jugador == numero_secreto:
            print("¡Felicidades! Ganaste.")
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
        jugar()

        respuesta = input("\n¿Quieres jugar otra vez? (s/n): ")

        if respuesta.lower() == "n":
            print("Gracias por jugar. ¡Hasta pronto!")
            break

        elif respuesta.lower() != "s":
            print("Respuesta no reconocida. Se iniciará otra partida.")


if __name__ == "__main__":
    main()
