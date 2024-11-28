
"""
Programa que pida 10 números e imprima el promedio de estos.

Se utilizan los conceptos del programa anterior de contador y acumulador.
"""
print("HOLA :)")

suma = 0
contador = 0

while contador < 10:
    numero = float(input("Ingresa un número: "))
    suma += numero
    contador += 1
promedio = suma / 10

print(f"El promedio de los 10 números es: {promedio}")
print("gracias por usarme. Creado por fer➤")