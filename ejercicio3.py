"""
Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma
y la media de todos los números introducidos.

Para este problema se requiere de un acumulador y un contador

Contador: Variable que va, como su nombre lo indica, contando elementos (iteraciones),
por cada iteración el contador va incrementando en 1

Ejemplo:
contador = 0
for i in range(5):
    contador = contador + 1
print(contador)

Acumulador: Variable que va, como su nombre lo indica, acumulando valores en cada iteración,
por cada iteración al valor inicial se le suman nuevos valores al acumulador

Ejemplo:
acumulador = 0;
for i in range(5):
    acumulador = acumulador + i
print(acumulador)
"""

print("HOLA :)")

contador = 0
acumulador = 0
while True:
    numero = int(input("Ingresa un número o introduce (0) para finilizar el programa: "))
    if numero == 0:
        break
    acumulador += numero
    contador += 1
if contador > 0:
    media = acumulador / contador
    print(f"La suma de los números ingresados es: {acumulador}")
    print(f"La media de los números ingresados es: {media}")
else:
    print("No se han introducido números válidos.")

print("gracias por usarme. Creado por fer➤")