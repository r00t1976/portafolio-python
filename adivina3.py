
import random
import json


ARCHIVO_HISTORIAL = "historial.json"


def cargar_historial():
    try:
        with open(ARCHIVO_HISTORIAL, "r", encoding="utf-8") as archivo:
            historial = json.load(archivo)

            if isinstance(historial, list):
                return historial

            return []

    except (FileNotFoundError, json.JSONDecodeError):
        return []


def guardar_historial(historial):
    with open(ARCHIVO_HISTORIAL, "w", encoding="utf-8") as archivo:
        json.dump(historial, archivo, indent=4, ensure_ascii=False)


def jugar(nivel, max_intentos):
    numero_secreto = random.randint(1, 100)
    intentos = 0

    print("\nNivel:", nivel)
    print("Adivina un número entre 1 y 100")
    print("Tienes", max_intentos, "intentos.")

    while intentos < max_intentos:
        try:
            numero_jugador = int(input("\nIngresa un número: "))

        except ValueError:
            print("Error: escribe un número entero.")
            continue

        if numero_jugador < 1 or numero_jugador > 100:
            print("El número debe estar entre 1 y 100.")
            continue

        intentos += 1

        if numero_jugador == numero_secreto:
            print("¡Felicidades! Ganaste.")

            return {
                "nivel": nivel,
                "intentos": intentos,
                "gano": True
            }

        elif numero_jugador < numero_secreto:
            print("El número secreto es mayor.")

        else:
            print("El número secreto es menor.")

        print("Intentos restantes:", max_intentos - intentos)

    print("\n¡Perdiste!")
    print("El número secreto era:", numero_secreto)

    return {
        "nivel": nivel,
        "intentos": intentos,
        "gano": False
    }


def mostrar_estadisticas(historial):
    victorias = 0

    for partida in historial:
        if partida["gano"]:
            victorias += 1

    print("\n===== ESTADÍSTICAS =====")
    print("Partidas jugadas:", len(historial))
    print("Partidas ganadas:", victorias)
    print("Partidas perdidas:", len(historial) - victorias)

    print("\nHistorial de partidas:")

    for numero, partida in enumerate(historial, start=1):
        print(
            "Partida:", numero,
            "| Nivel:", partida["nivel"],
            "| Intentos:", partida["intentos"],
            "| Ganó:", partida["gano"]
        )


def main():
    historial = cargar_historial()

    print("Bienvenido al juego de adivinanzas")
    print("Partidas anteriores:", len(historial))

    while True:
        print("\n===== MENÚ =====")
        print("1. Jugar nivel fácil")
        print("2. Jugar nivel medio")
        print("3. Jugar nivel difícil")
        print("4. Ver estadísticas")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nivel = "Facil"
            max_intentos = 10

        elif opcion == "2":
            nivel = "Medio"
            max_intentos = 7

        elif opcion == "3":
            nivel = "Dificil"
            max_intentos = 5

        elif opcion == "4":
            mostrar_estadisticas(historial)
            continue

        elif opcion == "5":
            print("Gracias por jugar.")
            break

        else:
            print("Opción incorrecta.")
            continue

        resultado = jugar(nivel, max_intentos)

        historial.append(resultado)
        guardar_historial(historial)

        print("\nPartida guardada correctamente.")
        mostrar_estadisticas(historial)


if __name__ == "__main__":
    main()
