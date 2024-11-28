"""
Algoritmo que pida caracteres e imprima 'VOCAL' si son vocales y 'NO VOCAL' en caso contrario, el programa termina cuando se introduce un espacio.

"""

print("HOLA :)")

while True:
    caracter = input("Ingresa un carácter: ")

    if caracter == ' ':
        break

    if caracter.lower() in 'aeiou':
        print("VOCAL")
    else:

        print("NO VOCAL")
print("gracias por usarme. Creado por fer➤")