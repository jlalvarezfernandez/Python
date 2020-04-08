import math

# Programa: Ejercicio13 raizCuadradaCubica.py
#
# Proposito:  Realizar un algoritmos que lea un número y que muestre su raíz cuadrada y su raíz cúbica. 
#             Python no tiene ninguna función predefinida que permita calcular la raíz cúbica, ¿cómo se puede calcular?
# 
#
# @author: Álvarez Fernández José Luis
# Fecha : 10/10/2019
#
#
# Variables a usar
# numero (númerica): almacenará el valor del número introducido 
# cuadrada (numérica): almacenará el resultado de la raiz cuadrada del número introducido
# cubica (numérica): almacenará el resultado de la raiz cúbica del número introducido
# 
#
# Algoritmo:
#
# LEER numero
# CALCULAR cuadrada, cubica
# ESCRIBIR cuadrada, cubica


# Pedimos al usuario que introduzca los datos por pantalla

numero = float(input("Introduce un número por pantalla: "))

# Calculos

cuadrada = "{0:.3f}".format(math.sqrt(numero))

cubica = "{0:.3f}".format(numero**(1/3))

# Mostramos los resultados por pantalla

print("La raiz cuadrada de", numero, " es: ", cuadrada)

print("La raiz cubica de", numero, " es: ", cubica)
