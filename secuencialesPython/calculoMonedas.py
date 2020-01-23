# Ejercicio 20 CalculoMonedas.py
#
# 20. Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos)
# después de pedirnos cuantas monedas tenemos de 2e, 1e, 50 céntimos, 20 céntimos o 10 céntimos).
#
# 
# @author: Álvarez Fernández José Luis
#


# Programa: Ejercicio20  CalculoMonedas.py
#
# Proposito:  Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos)
#             después de pedirnos cuantas monedas tenemos de 2e, 1e, 50 céntimos, 20 céntimos o 10 céntimos).
# 
#
# @author: Álvarez Fernández José Luis
# Fecha : 10/10/2019
#
#
# Variables a usar
# monedas2E (númerica): almacenará la cantidad de monedas de 2 euros (monedas2E * 2)
# monedas1E (númerica): almacenará la cantidad de monedas de 1 euro (monedas1E * 1)
# monedas50Cent (númerica): almacenará la cantidad de monedas de 50 centimos (monedas50Cent * 0.50)
# monedas20Cent (númerica): almacenará la cantidad de monedas de 20 centimos (monedas20Cent * 0.20)
# monedas10Cent (númerica): almacenará la cantidad de monedas de 10 centimos (monedas10Cent * 0.10)
# totalMonedas (númerica): almacenará la cantidad de dinero que tenemos (monedas2E + monedas1E + monedas50Cent + monedas20Cent + monedas10Cent)

# Algoritmo:
#
# LEER monedas2E, monedas1E, monedas50Cent, monedas20Cent, monedas10Cent
# CALCULAR totalMonedas
# ESCRIBIR totalMonedas


# Pedimos al usuario que introduzca los datos por pantalla


monedas2E = int(input("Introduce las monedas de 2 euros que tienes: "))
monedas1E = int(input("Introduce las monedas de 1 euro que tienes: "))
monedas50Cent = int(input("Introduce las monedas de 50 centimos que tienes: "))
monedas20Cent = int(input("Introduce las monedas de 20 centimos que tienes: "))
monedas10Cent = int(input("Introduce las monedas de 10 centimos que tienes: "))

# calculos

monedas2E = monedas2E * 2
monedas1E = monedas1E * 1
monedas50Cent = monedas50Cent * 0.50
monedas20Cent = monedas20Cent * 0.20
monedas10Cent = monedas10Cent * 0.10
totalMonedas = "{0:.2f}".format(monedas2E + monedas1E + monedas50Cent + monedas20Cent + monedas10Cent)


# Mostramos los resultados por pantalla

print("El total de monedas que tienes es de: ", totalMonedas , " Euros")


