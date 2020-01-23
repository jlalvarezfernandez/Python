'''
Programa: Ejercicio 19 E19DiasMes.py

Proposito: Escribe un programa que pida un número entero entre uno y doce e imprima el número de días que tiene el mes correspondiente.


@author: Álvarez Fernández José Luis

Fecha : 16/10/2019
'''
'''
variables a usar:
opcion (numérica): almacenará el valor de la opcion elegida del 1 al 12

Algoritmo:

LEER: opcion 
CALCULAR: creamos un menu con las diferentes opciones
ESCRIBIR: resultado
'''

# Pedimos al usuario que introduzca los datos por pantalla

opcion = int(input(" Introduce un número del 1 al 12 para saber cuantos dias tiene ese mes: "))

# Calculos

if opcion == 1:
    print("Enero tiene 31 dias")
elif opcion == 2:
    print("Febrero tiene 28 dias")
elif opcion == 3:
    print("Marzo tiene 31 dias")
elif opcion == 4:
    print("Abril tiene 30 dias")
elif opcion == 5:
    print("Mayo tiene 31 dias")
elif opcion == 6:
    print("Junio tiene 30 dias")
elif opcion == 7:
    print("Julio tiene 30 dias")
elif opcion == 8:
    print("Agosto tiene 31 dias")
elif opcion == 9:
    print("Septiembre tiene 30 dias")
elif opcion == 10:
    print("Octubre tiene 31 dias")
elif opcion == 11:
    print("Noviembre tiene 30 dias")
elif opcion == 12:
    print("Diciembre tiene 31 dias")
else:
    print("ERROR!!!, NÚMERO INCORRECTO")