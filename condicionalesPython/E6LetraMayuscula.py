'''
Programa: Ejercicio 6 E6LetraMayuscula.py

Proposito: Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.

@author: Álvarez Fernández José Luis

Fecha : 16/10/2019
'''
'''
variables a usar:
cadena (string): almacenará el valor de la cadena introducida


Algoritmo:

LEER: cadena    
CALCULAR: si la cadena introducida esta escrita con mayuscula o no (usaremos la funcion issupper, 
que devuelve si la cadena esta escrita en mayusculas o no)
ESCRIBIR: resultado
'''

# Pedimos al usuario que introduzca los datos por pantalla

cadena = (input("Introduce una cadena por teclado: "))

# Calculos

if cadena.isupper():
    print("Esta escrito en mayusculas")
else:
    print("Esta escrito en minusculas")