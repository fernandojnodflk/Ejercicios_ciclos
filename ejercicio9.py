"""
Escribe un programa que pida el limite inferior y superior de un intervalo.
Si el límite inferior es mayor que el superior lo tiene que volver a pedir.
A continuación se van introduciendo números hasta que introduzcamos el 0.
Cuando termine el programa dará las siguientes informaciones:
	* La suma de los números que están dentro del intervalo (intervalo abierto).
	* Cuantos números están fuera del intervalo.
	* He informa si hemos introducido algún número igual a los límites del intervalo.
"""

print("HOLA :)")

while True:
    limite_inferior = int(input("Ingresa el límite inferior del intervalo: "))
    limite_superior = int(input("Ingresa el límite superior del intervalo: "))

    if limite_inferior < limite_superior:
        break

    print("El límite inferior debe ser menor que el límite superior. Intenta nuevamente.")

suma_intervalo = 0
fuera_intervalo = 0
numero_igual_limite = False

while True:
    numero = int(input("Ingresa un número (0 para terminar): "))

    if numero == 0:
        break


    if limite_inferior < numero < limite_superior:
        suma_intervalo += numero
    elif numero == limite_inferior or numero == limite_superior:
        numero_igual_limite = True
    else:
        fuera_intervalo += 1

print("\nResultados:")
print(f"La suma de los números dentro del intervalo es: {suma_intervalo}")
print(f"Cantidad de números fuera del intervalo: {fuera_intervalo}")
if numero_igual_limite:
    print("Se introdujo un número igual a los límites del intervalo.")
else:
    print("No se introdujo ningún número igual a los límites del intervalo.")

print("gracias por usarme. Creado por fer➤")