import math

# Programa: Ejercicio3 hipotenusa.py
#
# Proposito: Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
#
# @author: Álvarez Fernández José Luis
# Fecha : 10/10/2019
#
#
# Variables a usar
# cateteo1 (númerica): almacenará el valor del primer cateto
# cateto2 (numérica): almacenará el valor del segundo cateto
# hipotenusa (numérica): almacenará la hipotenusa del triangulo rectángulo (math.sqrt(cateto1**2 + cateto2**2))
#
# Algoritmo:
#
# LEER cateto1, cateto2
# CALCULAR hipotenusa 
# ESCRIBIR hipotenusa


#Pedimos al usuario que introduzca los datos por pantalla
cateto1 = float(input("Introduce el valor del cateto 1: "))

cateto2 = float(input("Introduce el valor del cateto 2: "))


#Calculos

hipotenusa = (math.sqrt(cateto1**2 + cateto2**2))

#Mostramos los resultados por pantalla

print("La hipotenusa del triangulo rectangulo dados tus catetos es de: ", hipotenusa)
