"""
Mostrar en pantalla los N primero números primos. Se pide por teclado la cantidad
de números primos que queremos mostrar.
"""

print("HOLA :)")

def es_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

n_primos = int(input("Ingresa la cantidad de números primos que deseas mostrar: "))
contador = 0
numero = 2

while contador < n_primos:
    if es_primo(numero):
        print(numero)
        contador += 1
    numero += 1

print("gracias por usarme. Creado por fer➤")