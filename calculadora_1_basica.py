"""Calculadora 1 - La más básica.
Usa print/input y variables, sin funciones ni bucles.
"""

print("=== Calculadora básica ===")
a = float(input("Primer número: "))
b = float(input("Segundo número: "))

print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
if b != 0:
    print("División:", a / b)
else:
    print("División: no se puede dividir por cero")
