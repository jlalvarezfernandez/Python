'''
Programa: Ejercicio 4 E04numerosPares.py

Proposito: Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.

@author: Álvarez Fernández José Luis

Fecha : 22/10/2019

'''
'''
Variables:
num1 (numérica): almacenará el primer número introducido por el usuario
num2 (numérica): almacenará el segundo número introducido por el usuario

Algoritmo:

LEER: num1, num2
CALCULAR: bucle while para corregir error de introducir el segundo número menor que el primero.
		  bucle for-in con el primer argumento que sea num1, el segundo num2, y el tercero será un incremento de 1
		  condicional if para clacular si un numero es par (aquel que dividido entre 2 su resto es cero)
ESCRIBIR: numeros

'''

# Pedimos al usuario que introduzca la información por pantalla

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

# Calculos
while num2 < num1:
	print("El primer número debe de ser mas pequeño que el grande")
	num1 = int(input("Introduce el primer número: "))
	num2 = int(input("Introduce el segundo número: "))

for numeros in range (num1,num2,1):
	if (numeros%2 == 0):	
		print(numeros)
				
		