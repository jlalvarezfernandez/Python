'''
Programa: Ejercicio 8 E08cronometro.py

Proposito: Hacer un programa que muestre un cronometro, indicando las horas, minutos y segundos.
           Para hacer una espera en Python podemos usar el método sleep del módulo time.

@author: Álvarez Fernández José Luis

Fecha : 26/10/2019

'''

'''
Variables: horas, minutos, segundos

Algoritmo: 

CALCULAR: importamos el metodo time para poder usar despues la funcion sleep a la que introduciremos 
          como parametro 1 en referencia al intervalo de tiempo que transcurra en nuestro cronometro.
          creamos un bucle for para las horas que vaya de 0 hasta 24 horas
          creamos un bucle for para contar los segundos de 0 a 60
          creamos un bucle for para contar los segundos de 0 a 60
ESCRIBIR: horas, minutos, segundos

'''
#importamos el metodo time
import time


# Calculos

for horas in range (0,24):
    for minutos in range (0,60):
        for segundos in range (0,60):
            print(f"{horas:02}:{minutos:02}:{segundos:02}", end="")
            time.sleep(1)
            print(8 * "\b", end="") 
            
            
'''
horas = 0
minutos = 0
segundos = 0

#proceso
#hacemos un ciclo infinito y esperamos 1 segundo cada iteracion

while true:
    print(f"{horas:02}:{minutos:02}:{segundos:02}", end="")
    time.sleep(1)
    # pasar al siguiente segundo
    if segundos < 59:
      segundos +=1
    else:
      segundos = 0
      if minutos <59:
        minutos+=1
      else:
        minutos = 0
        horas +=1
        
        print(8 * "\b", end="")

'''


