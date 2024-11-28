"""
Crea un programa que permita adivinar un número. La aplicación genera un
número aleatorio del 1 al 100. A continuación va pidiendo números y va
respondiendo si el número a adivinar es mayor o menor que el introducido,
a demás de los intentos que te quedan (tienes 10 intentos para acertarlo).
El programa termina cuando se acierta el número (además te dice en cuantos
intentos lo has acertado), si se llega al limite de intentos te muestra el
número que había generado.
Para genear un número entero aleatorio se utiliza la función randint
del paquete random

import random
aleatorio = random.randint(limite_inf, limite_sup)
"""

print("HOLA :)")
import random
numero_aleatorio = random.randint(1, 100)
intentos_maximos = 10
intentos = 0

print("¡Bienvenido a mi juego de adivinar un numero al hazar!")
print("Este programa genera un número aleatorio entre 1 y 100. Tienes 10 intentos para adivinarlo.🍀Suerte🍀")

while intentos < intentos_maximos:
    intentos += 1
    intento_usuario = int(input(f"Intento {intentos}/{intentos_maximos}: Introduce un número: "))
    if intento_usuario == numero_aleatorio:
        print(f"¡Felicidades! Has adivinado el número en {intentos} intentos.")
        break
    elif intento_usuario < numero_aleatorio:
        print("El número es mayor. ¡Sigue intentando!")
    else:
        print("El número es menor. ¡Sigue intentando!")
    if intentos == intentos_maximos:
        print(f"Lo siento, has agotado todos tus intentos:(   El número era {numero_aleatorio}.")

print("gracias por usarme. Creado por fer➤")