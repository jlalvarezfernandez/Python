'''
Programa: Ejercicio 8 E8NotaYEdad.py

Proposito: Algoritmo que pida dos números ‘nota’ y ‘edad’ y un carácter ‘sexo’ y muestre el 
           mensaje ‘ACEPTADA’ si la nota es mayor o igual a cinco, la edad es mayor o igual a 
           dieciocho y el sexo es ‘F’. En caso de que se cumpla lo mismo, pero el sexo sea ‘M’, debe 
           imprimir ‘POSIBLE’. Si no se cumplen dichas condiciones se debe mostrar ‘NO ACEPTADA’.

@author: Álvarez Fernández José Luis

Fecha : 16/10/2019
'''
'''
variables a usar:
nota (numérica): almacenará el valor de la nota
edad (numérica): almacenará la edad
sexo (string): alamcenará el sexo, si es hombre o mujer


Algoritmo:

LEER: nota, edad, sexo 
CALCULAR: realizamos el condicional if con las diferentes opciones a elegir
if nota >=5 and edad >=18 and sexo =="F":
    print("ACEPTADA")
elif nota >=5 and edad >=18 and sexo =="M":
    print("POSIBLE")
else:
    print("NO ACEPTADA")
ESCRIBIR: resultado
'''

# Pedimos al usuario que introduzca los datos por pantalla

nota = float(input("Introduce la nota: "))

edad = int(input("Introduce tu edad: "))

sexo = input("Introduce el sexo: ('F' o 'M') ")

# Calculos

if nota >=5 and edad >=18 and sexo =="F" or sexo =='f':
    print("ACEPTADA")
elif nota >=5 and edad >=18 and sexo =="M" or sexo == 'm':
    print("POSIBLE")
else:
    print("NO ACEPTADA")
