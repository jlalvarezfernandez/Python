import math
# Programa: Ejercicio12 puntosPlano.py
#
# Proposito:  Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos en el plano. Calcula y muestra la distancia entre ellos.
# 
#
# @author: Álvarez Fernández José Luis
# Fecha : 10/10/2019
#
#
# Variables a usar
# x1 (númerica): almacenará el valor de x1 
# x2 (númerica): almacenará el valor de x2
# y1 (númerica): almacenará el valor de y1 
# y2 (númerica): almacenará el valor de y2
# distancia(númerica): almacenará la distancia que hay entre los números (math.sqrt(x2 - x1)**2 + (y2 - y1)**2)
# 
#
# Algoritmo:
#
# LEER x1, x2, y1. y2
# CALCULAR distancia 
# ESCRIBIR distancia

# Pedimos al usuario que introduzca la informacion por pantalla

x1 = float(input("Introduce el valor de x1: "))
x2 = float(input("Introduce el valor de x2: "))
y1 = float(input("Introduce el valor de y1: "))
y2 = float(input("Introduce el valor de y2: "))

# Calculos

distancia = (math.sqrt(math.pow((x2 - x1),2) + math.pow((y2 - y1),2)))

# Mostramos los resultados por pantalla

print("La distancia entre los numeros introducidos es de: ",  "{0:.2f}".format(distancia))



