'''
Programa: Ejercicio 1 E1mayorOMenor.py

Proposito: Algoritmo que pida dos números e indique si el primero es mayor que el segundo o no.

@author: Álvarez Fernández José Luis

Fecha : 16/10/2019

'''
'''
variables a usar:
num1 (numérica): almacenará el valor del primer número
num2 (numércia): almacenaráel valor del segundo número

Algoritmo:

LEER: num1, num2       
CALCULAR: si num1 es mayor que num2 o no (estructura condicional)
ESCRIBIR: resultado
'''

# Pedimos al usuario que introduzca los datos por pantalla

num1 = float(input("Introduce el valor del primer número: "))
num2 = float(input("Introduce el valor del segundo número: "))

# Calculos

if num1 > num2:
    print("El primer número es mayor que el segundo número introducido")
else:
    print("El segundo número es mayor que el primer número introducido")



