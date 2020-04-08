'''
Programa: Ejercicio 14 E014subcadena.py

Proposito: Realizar un programa que compruebe si una cadena contiene una subcadena. Las dos cadenas se introducen por teclado.

@author: Álvarez Fernández José Luis

Fecha : 26/10/2019

'''

'''
Variables:
cadena (cadena): almacenará la frase introducida por el usuario
subcadena (cadena): almacenará la subcadena que queremos comprobar si aparece en la cadena primaria

Algoritmo:
LEER: cadena, subcadena
CALCULAR: bucle while mientras cadena y subcadena sea diferentas a una cadena vacia
          creamos un condicional para comprobar que si la subcadena es mayor que cero la busque y la mostramos por pantalla
          si no se mostrará que esa subcadena no pertenece a la cadena primaria.

'''
# Pedimos al usuario que ontroduzca los datos por pantalla

cadena = str(input("Introduce una frase: "))
subcadena = str(input("Introduce una subcadena de la frase anterior: "))


# Calculos
'''
while cadena != "" or subcadena != "":
    if cadena.find(subcadena) >=0:
	    print("Aparece la subcadena",subcadena,"de la cadena principal")
    else:
	    print("La subcadena introducida no pertenece a la cadena principal")
    cadena= str(input("Programa terminado"))
'''


