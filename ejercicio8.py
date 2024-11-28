"""
Escribir un programa que imprima todos los números pares entre dos números que
se le pidan al usuario.
"""

print("HOLA :)")

inicio = int(input("Ingresa el primer número: "))
fin = int(input("Ingresa el segundo número: "))

if inicio > fin:
    inicio, fin = fin, inicio

for numero in range(inicio, fin + 1):
    if numero % 2 == 0:

        print( "El numero par es:" + str(numero))
print("gracias por usarme. Creado por fer➤")