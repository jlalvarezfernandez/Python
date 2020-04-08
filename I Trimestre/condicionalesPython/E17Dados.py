'''
Programa: Ejercicio 17 E17Dados.py

Proposito: Realiza un programa que pida por teclado el resultado (dato entero) obtenido al lanzar un dado de seis caras 
           y muestre por pantalla el número en letras (dato cadena) de la cara opuesta al resultado obtenido.
                Nota 1: En las caras opuestas de un dado de seis caras están los números: 1-6, 2-5 y 3-4.
                Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, 
                se mostrará el mensaje: “ERROR: número incorrecto.”.

@author: Álvarez Fernández José Luis

Fecha : 16/10/2019
'''
'''
variables a usar:
opcion (numérica): almacenará el valor de la opcion elegida del 1 al 6



Algoritmo:

LEER: opcion 
CALCULAR: creamos un menu con las diferentes opciones
ESCRIBIR: resultado
'''

# Pedimos al usuario que introduzca los datos por pantalla

opcion = int(input("Introduce un número del 1 al 6: "))

# Calculos

if opcion == 1:
    print("En la cara opuesta del 1 esta el 6")

elif opcion == 2:
    print("En la cara opuesta del 2 esta el 5")

elif opcion == 3:
    print("En la cara opuesta del 3 esta el 4")

elif opcion == 4:
    print("En la cara opuesta del 4 esta el 3")

elif opcion == 5:
    print("En la cara opuesta del 5 esta el 2")

elif opcion == 6:
    print("En la cara opuesta del 6 esta el 1")

else:
    print("ERROR!!! número incorrecto")



