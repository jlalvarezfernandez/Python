'''
Programa: Ejercicio 1 E01aleatorio.py

Proposito: Crea una aplicación que permita adivinar un número. 
           La aplicación genera un número aleatorio del 1 al 100. 
           A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor 
           que el introducido,
           además de los intentos que te quedan (tienes 10 intentos para acertarlo). 
           El programa termina cuando se acierta el número (además te dice en cuantos intentos
           lo has acertado), 
           si se llega al limite de intentos te muestra el número que había generado.

@author: Álvarez Fernández José Luis

Fecha : 22/10/2019

'''
'''
variables a usar:
aleatorio (numérica): almacenará el número aleatorio, para eso usamos la función random.randint
contador (numérica): usamos un contador iniciando en 0 para que nos cuente los intentos que llevamos, y despues de cada intento
                     iremos sumandole uno.
número (numérica): almacenará el número introducido por el usuario.

Algoritmo:

Creamos el número aleatorio con la función random.randint  
Creamos un bucle for ya que sabemos de antemano los intentos de los que vamos a disponer (10)
dentro de ese bucle creamos un condicional if.. else con las dos posibles opciones: que acertemos el número o que no,
si acertamos el número se rompe el condicional y ya sale del bucle para informar al usuario del número que era 
y de los intentos necesitados.
si no acertamos el número, a continiacion nos dira gracias a otro condicional if..else si el número que hemos introducido 
es mayor o menor que el aleatorio.
ESCRIBIR: aleatorio y contador
'''
# importamos la función random para generar número aleatorios

import random

aleatorio = random.randint(1,100)
contador = 0

# Calculos

for numero in range (1,11):
    numero = int(input("Introduce un número entre el 1 y el 100: "))
    
    if numero == aleatorio:
        print("Has acertado!!!")
        contador +=1
        break
    else:
        print("No has acertado")
    if numero < aleatorio:
        print("El número introducido es menor que el número aleatorio, vuelve a intentarlo")
        contador +=1
    else:
        numero > aleatorio
        print("El número introducido es mayor que el número aleatorio, vuelve a intentarlo")
        contador +=1

# Mostramos los resultados por pantalla

print("El número aleatorio es: ", aleatorio, "y has necesitado", contador, "intentos")
    
    



