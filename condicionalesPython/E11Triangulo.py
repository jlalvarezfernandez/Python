'''
Programa: Ejercicio 11 E11Triangulo.py

Proposito: Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los lados de un triángulo.
           El programa debe determinar que tipo de triangulo es, teniendo en cuenta los siguiente:
                Si se cumple Pitágoras entonces es triángulo rectángulo
                Si sólo dos lados del triángulo son iguales entonces es isósceles.
                Si los 3 lados son iguales entonces es equilátero.
                Si no se cumple ninguna de las condiciones anteriores, es escaleno.


@author: Álvarez Fernández José Luis

Fecha : 17/10/2019
'''
'''
variables a usar:
ladoA (numérica): almacenará el valor de un lado del triangulo
ladoB (numérica): almacenará el valor de un lado del triangulo
ladoC (numérica): almacenará el valor de un lado del triangulo


Algoritmo:

LEER: ladoA, ladoB, ladoC   
CALCULAR: para calcular si es un triángulo rectangulo recurrimos a la formula a2 = b2 + c2 y ponemos las diversas opciones
          para calcular si es un triangulo isosceles comparamos dos lados que tienen que ser iguales 
          y el otro debe de ser diferente longutud 
          para calcular si es un triángulo equilatero los 3 lados deben de ser iguales
          para calcular si es un triángulo escaleno la longitus de los lado debe ser diferente.
ESCRIBIR: resultado
'''
import math

# Pedimos al usuario que introduzca los datos por pantalla

ladoA = float(input("Introduce el valor del lado A: "))
ladoB = float(input("Introduce el valor del lado B: "))
ladoC = float(input("Introduce el valor del lado C: "))

# Calculos

if math.pow(ladoA,2) == math.pow(ladoB,2)+math.pow(ladoC,2) or math.pow(ladoB,2) == math.pow(ladoC,2)+math.pow(ladoB,2) or math.pow(ladoC,2) == math.pow(ladoA,2)+math.pow(ladoB,2):
    print("Cumple Pitagoras, por lo que es un triangulo rectángulo")   
elif ladoA == ladoB and ladoA != ladoC or ladoB == ladoC and ladoB != ladoA or ladoC == ladoA and ladoC != ladoB:
    print("es un triángulo Isosceles")
elif ladoA == ladoB and ladoC == ladoB:
    print("Los 3 lados son iguales, por lo que es un triángulo equilátero.")                                               
else: 
    print("No cumple ninguna de las condiciones anteriores por lo que es un triangulo escaleno.")
