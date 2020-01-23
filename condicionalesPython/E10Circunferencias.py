'''
Programa: Ejercicio 10 E10Circunferencias.py

Proposito: Algoritmo que pida los puntos centrales x1,y1,x2,y2 y los radios r1,r2 de dos circunferencias
           y las clasifique en uno de estos estados:

                exteriores
                tangentes exteriores
                secantes
                tangentes interiores
                interiores
                concéntricas


@author: Álvarez Fernández José Luis

Fecha : 17/10/2019
'''
'''
variables a usar:
x1 (numérica): almacenará el valor de un punto central de la circunferencia 1
y1 (numérica): almacenará el valor de un punto central de la circunferencia 1
x2 (numérica): almacenará el valor de un punto central de la circunferencia 2
y2 (numérica): almacenará el valor de un punto central de la circunferencia 2
r1 (numérica): almaenará el valor del radio de la primera circunferencia
r2 (numérica): almaenará el valor del radio de la segunda circunferencia



Algoritmo:

LEER: x1,y1,x2,y2  
CALCULAR: definimos la variable distancia para calcular la diferencia entrre los puntos de las 
          dos circunferencias (distancia = (math.sqrt(math.pow((x2 - x1),2) + math.pow((y2 - y1),2))))
          aplicamos la formula (distancia > (r1 + r2)) para saber si son circunferencias exteriores
          aplicamos la formula (distancia < (r1 +r2) and distancia > (r1 -r2)) para saber si son circunferencias secantes          
          aplicamos la formula (distancia == (r1 + r2)) para saber si son circunferencias tangentes exteriores
          aplicamos la formula (distancia == (r1 - r2)) para saber si son circunferencias tangentes interiores
          si no cumplen ninguna de estas condiciones nos encontramos ante circunferencias concentricas
ESCRIBIR: resultado
'''
import math

# Pedimos al usuario que introduzca los datos por pantalla

x1 = float(input("Introduce el valor del punto central x1 de la primera circunferencia: "))
y1 = float(input("Introduce el valor del punto central y1 de la primera circunferencia: "))
x2 = float(input("Introduce el valor del punto central x2 de la segunda circunferencia: "))
y2 = float(input("Introduce el valor del punto central y2 de la segunda circunferencia: "))
r1 = float(input("Introduce el radio de la primera circunferencia: "))
r2 = float(input("Introduce el radio de la segunda circunferencia: "))


# Calculos

distancia = (math.sqrt(math.pow((x2 - x1),2) + math.pow((y2 - y1),2)))

if distancia > (r1 + r2):
    print("se trata de circunferencias exteriores, no tienen puntos en comun")

elif distancia < (r1 +r2) and distancia > (r1 -r2):
    print("Se tratan de circunferencias secantes, tienen dos puntos en común")

elif distancia > 0 and distancia < (r1 - r2):
    print("se trata de circunferencias interiores, una esta dentro de la otra")

elif distancia == (r1 + r2):
    print("se trata de circunferencias tangentes exteriores")

elif distancia == (r1 - r2):
    print("se trata de circunferencias tangentes interiores")

else:
    print("se trata de circunferencias concentricas")

