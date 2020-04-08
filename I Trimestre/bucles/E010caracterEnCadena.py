'''
Programa: Ejercicio 10 E010caracterEnCadena.py

Proposito: Pide una cadena y un carácter por teclado y muestra cuantas veces aparece el carácter en la cadena.

@author: Álvarez Fernández José Luis

Fecha : 26/10/2019

'''

'''
Variables:
cadena (cadena): almacenará la frase introducida por el usuario
caracterIntroducido (cadena): almacenará el caracter que queremos ver cuantas veces se repite en la cadena

Algoritmo:

LEER: cadena, caracterIntroducido
CALCULAR: creamos un contador para que vaya sumando cuantas veces aparece repetiod ese caracter, al principio 
          inicializado en 0 y al que despues le sumaremos uno por cada vez que se repita el caracter
          creamos un bucle for en el que pedimos que le caracterIntroducido se incremente en uno 
ESCRIBIR: caracterIntroducido, contador

'''
# Pedimos al usuario que introduzca losdatos por pantalla

cadena = str(input("Introduce una cadena: "))
caracterIntroducido = str(input("Introduce un caracter: "))
contador = 0

# Calculos

for i in cadena:
        if i == caracterIntroducido:
            contador +=1

# Mostramos los resultados por pantalla

print("El caracter introducido es: ",caracterIntroducido,"y aparece:",contador,"veces")

