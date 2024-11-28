"""
Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10
euros, el segundo 20 euros, el tercero 40 euros y así sucesivamente.
Realizar un programa para determinar cuánto debe pagar mensualmente y el totals
de lo que pagó después de los 20 meses.
"""

print("HOLA :)")
total_pagado = 0


for mes in range(1, 21):

    pago_mes = 10 * (2 ** (mes - 1))
    total_pagado += pago_mes

    print(f"Mes {mes}: {pago_mes} euros")
print(f"\nTotal pagado después de 20 meses: {total_pagado} euros")
print("gracias por usarme. Creado por fer➤")