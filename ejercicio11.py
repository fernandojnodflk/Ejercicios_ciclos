"""
Escribe un programa que diga si un número introducido por teclado es o no primo.
Un número primo es aquel que sólo es divisible entre él mismo y la unidad.
Nota: Es suficiente probar hasta la raíz cuadrada del número para ver si es
divisible por algún otro número.
"""

print("HOLA :)")

import math

numero = int(input("Ingresa un número entero: "))

def es_primo(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    limite = int(math.sqrt(num)) + 1
    for i in range(3, limite, 2):
        if num % i == 0:
            return False
    return True

if es_primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")
print("gracias por usarme. Creado por fer➤")