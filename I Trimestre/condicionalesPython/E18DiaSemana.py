'''
Programa: Ejercicio 18 E18DiaSemana.py

Proposito: Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día correspondiente. 
           Si introducimos otro número nos da un error.



@author: Álvarez Fernández José Luis

Fecha : 16/10/2019
'''
'''
variables a usar:
opcion (numérica): almacenará el valor de la opcion elegida del 1 al 7

Algoritmo:

LEER: opcion 
CALCULAR: creamos un menu con las diferentes opciones
ESCRIBIR: resultado
'''

# Pedimos al usuario que introduzca los datos por pantalla

opcion = int(input(" Introduce un número del 1 al 7 para saber a que dia de la semana corresponde: "))

# Calculos

if opcion == 1:
    print("Lunes")
elif opcion == 2:
    print("Martes")
elif opcion == 3:
    print("Miercoles")
elif opcion == 4:
    print("Jueves")
elif opcion == 5:
    print("Viernes")
elif opcion == 6:
    print("Sabado")
elif opcion == 7:
    print("Domingo")
else:
    print("ERROR!!!, NÚMERO INCORRECTO")