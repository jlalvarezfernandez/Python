'''
Programa: Ejercicio 13 E013mayusculasMinusculas.py

Proposito: Realizar un programa que lea una cadena por teclado y convierta las mayúsculas a minúsculas y viceversa.


@author: Álvarez Fernández José Luis

Fecha : 26/10/2019

'''

'''
Variables:
cadena (cadena): almacenará la frase que el usuario introduzca
mayusculas (cadena): alamcenará la cadena en mayusculas
minusculas (cadena): alamcenará la cadena en minusculas

Algoritmo:
LEER: cadena
CALCULAR: bucle while, mientras no se introduzca una cadena vacia 
          hacemos un condicional que pasa la cadena a mayusculas y sino la pasa a minusculas



'''
# Pedimos al usuario que introduzca los datos por pantalla

cadena = str(input("Introduce una cadena: "))
mayusculas = cadena.upper()
minusculas = cadena.lower()

# Calculos

while cadena != "":
    if cadena == mayusculas:
        print(minusculas)
    else:
        cadena == minusculas
        print(mayusculas)
    cadena =str(input("Fin programa"))
