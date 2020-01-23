'''
Programa: Ejercicio 3 E3ParOImpar.py

Proposito: Escribe un programa que lea un número e indique si es par o impar.

@author: Álvarez Fernández José Luis

Fecha : 16/10/2019

'''
'''
variables a usar:
num (numérica): almacenará el valor del número introducido


Algoritmo:

LEER: num      
CALCULAR: si el número introducido es par o impar 
(sabemos que un número es par, cuando se puede dividir entre 2 y su resto es cero, 
e impar cuando su resto no es 0)
ESCRIBIR: resultado
'''

# Pedimos al usuario que introduzca los datos por pantalla

num = int(input("Introduce un número para saber si es par o impar: "))

# Calculos


if num%2 == 0:
    print("El número introducido es par")
else:
    print("El número introducido es impar")