
'''
Programa: Ejercicio 6 E06potencia.py

Proposito: Escribe un programa que dados dos números, uno real (base) y un entero positivo (exponente),
           saque por pantalla el resultado de la potencia. No se puede utilizar el operador de potencia.

@author: Álvarez Fernández José Luis

Fecha : 26/10/2019

'''
'''
Variables:

base (numérica): almacenará la base de la potencia
exponente (numérica): almacenará el exponente d ela potencia
resultado (numérica): iniciado a 1 porque si el exponente es 1 el resultado será de 1

Algoritmo:

LEER base, exponente
CALCULAR: ciclo for-in con 2 argumentos, el primero 0(no sabemos la base introducida) y el segundo será el exponente
          para calcular la potencia sabemos que será el resultado de multiplicar la base por el número de veces del exponente introducido
ESCRIBIR: resultado
'''
# Pedimos al usuario que introduzca los datos por pantalla

base = float(input("Introduce un número real como base de la potencia: "))
exponente = int(input("Introduce un número entero como exponente de la potencia: "))
resultado = 1

# Calculos

for potencia in range (0,exponente):  
    resultado *= base

# Mostramos el re4sultado por pantalla
 
print("la potencia es: ",resultado)