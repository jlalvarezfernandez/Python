'''
Programa: Ejercicio 12 E12AnnioBisiesto.py

Proposito: Escribir un programa que lea un año indicar si es bisiesto. 
          Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100, 
          excepto que también sea divisible por 400.



@author: Álvarez Fernández José Luis

Fecha : 17/10/2019
'''
'''
variables a usar:
annio (numérica): almacenará el valor de la cadena introducida


Algoritmo:

LEER: annio    
CALCULAR: si el resto del año intruducido y dividido entre 4 o 400 es cero el año es bisiesto 
ESCRIBIR: resultado
'''

# Pedimos al usuario que introduzca los datos por pantalla

annio = int(input("Introduce un año para saber si es bisiesto o no: "))

# Calculos
if annio % 4 == 0 or annio % 400 == 0 and annio % 100 != 0:
    print("El año introducido es bisiesto")
else:
    print("El año introducido no es bisiesto")