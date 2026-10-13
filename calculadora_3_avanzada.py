"""Calculadora 3.0 - Avanzada.
Usa diccionario de funciones, historial de operaciones y archivos.
"""

import json
from datetime import datetime

# librerias que se usaran para el historial de operaciones y funciones matematicas  #

HISTORIAL_PATH = "historial.json"

# aca comienzan las funciones que vamos utilizar e operadoras matematicos  #

def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("División por cero")
    return a / b


def potencia(a, b):
    return a ** b

# arriba muestra libreria de historial y funciones de operaciones matematicas  #

OPERACIONES = {
    "+": sumar,
    "-": restar,
    "*": multiplicar,
    "/": dividir,
    "**": potencia,
}


def cargar_historial():
    try:
        with open(HISTORIAL_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def guardar_historial(historial):
    with open(HISTORIAL_PATH, "w", encoding="utf-8") as f:
        json.dump(historial, f, indent=2, ensure_ascii=False)

# cambie y agregue mas personalizacion a la barra de opciones, dando mas  color para distinguir  y mas informacion de como usar la calculadora  #

def main():
    historial = cargar_historial()
    print("=============================> Calculadora avanzada <============================")
    print("Operaciones: +  -  *  /  **")
    print("Escribe \033[32m'historial\033[0m' para ver el historial, \033[31m'salir\033[0m' para terminar.\n")

    while True:
        entrada = input("Ingresa: número1 operación número2 → ").strip()

        if entrada.lower() == "salir":
            break
        if entrada.lower() == "historial":
            for h in historial[-5:]:
                print(f"  {h['fecha']}: {h['expresion']} = {h['resultado']}")
            continue

        try:
            a_str, op, b_str = entrada.split()
            a, b = float(a_str), float(b_str)
            if op not in OPERACIONES:
                print("Operación no válida. Usa:", ", ".join(OPERACIONES))
                continue
            resultado = OPERACIONES[op](a, b)
            print("Resultado:", resultado)
            historial.append(
                {
                    "fecha": datetime.now().strftime("%Y-%m-%d %H:%M"),
                    "expresion": f"{a} {op} {b}",
                    "resultado": resultado,
                }
            )
            guardar_historial(historial)
        except ValueError:
            print("Formato: 10 + 5")
        except ZeroDivisionError as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
