"""
Realizar un programa para determinar cuánto ahorrará una persona en un año,
si al final de cada mes deposita cantidades variables de dinero;
además, se quiere saber cuánto lleva ahorrado cada mes.
"""

print("HOLA :)")

ahorro_total = 0
for mes in range(1, 13):

    deposito_mes = float(input(f"Ingresa la cantidad ahorrada en el mes {mes}: "))

    ahorro_total += deposito_mes

    print(f"Ahorro acumulado hasta el mes {mes}: {ahorro_total:.2f} unidades monetarias")


print(f"\nTotal ahorrado al final del año: {ahorro_total:.2f} unidades monetarias")
print("gracias por usarme. Creado por fer➤")