'''
Programa: Ejercicio 4 E4Division.py

Proposito: Crea un programa que pida al usuario dos números y muestre su división si el segundo no es cero, o un mensaje de aviso en caso contrario.

@author: Álvarez Fernández José Luis

Fecha : 16/10/2019

'''
'''
variables a usar:
num1 (numérica): almacenará el valor del primer número introducido
num2 (numérica): almacenará el valor del segundo número introducido
resultado (numérica): alamcenará el resultado de la división

Algoritmo:

LEER: num1, num2, resultado     
CALCULAR: mostrar division de los dos números mientras el segundo número no sea 0
ESCRIBIR: resultado
'''

# Pedimos al usuario que introduzca los datos por pantalla

num1 = float(input("Introduce el valor del primer número: "))
num2 = float(input("Introduce el valor del segundo número: "))

# Calculos

if num2 == 0:
    print("Error!!!!! el número introducido es un 0, vuelve a intentarlo")
else:
    print("El resultado de dividir los dos números es: ", (num1/num2))



