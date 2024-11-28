"""
Escribe un programa que dados dos números, uno real (base) y un entero positivo
(exponente), saque por pantalla el resultado de la potencia. No se puede
utilizar el operador de potencia.
"""


print("HOLA :)")

base = float(input("Ingresa la base (número real): "))
exponente = int(input("Ingresa el exponente (entero positivo): "))

if exponente < 0:
    print("El exponente debe ser un número entero positivo.")
else:
    resultado = 1


    for _ in range(exponente):
        resultado *= base

    print(f"El resultado de {base} elevado a la {exponente} es: {resultado}")
print("gracias por usarme. Creado por fer➤")