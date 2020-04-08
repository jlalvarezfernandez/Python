'''
Programa: Ejercicio 7 E7Potencia.py

Proposito: Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el exponente.Pueden ocurrir tres cosas:

                El exponente sea positivo, sólo tienes que imprimir la potencia.
                El exponente sea 0, el resultado es 1.
                El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.

@author: Álvarez Fernández José Luis

Fecha : 16/10/2019
'''
'''
variables a usar:
base (numérica): almacenará el valor de la  base
exponente (numérica): almacenará el valor del exponente
resultado (numérica): alamcenará el resultado de la potencia


Algoritmo:

LEER: base , exponente  
CALCULAR: según sea el valor del exponente introducido realizar unas operaciones u otras
ESCRIBIR: resultado
'''

# Pedimos al usuario que introduzca los datos por pantalla

base = int(input("Introduce la base de la potencia: "))
exponente = int(input("Introduce el exponente de la potencia: "))

# Calculos

resultado = base**exponente
print("El resultado de la potencia es: ", resultado)

if exponente > 0:
    print("El resultado de la potencia es: ", resultado)
elif exponente == 0:
    print(" El resultado de la potencia es 1")
else:
    print("El resultado de la potencia es 1/potencia con el exponente positivo.")