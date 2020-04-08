'''
Programa: Ejercicio 11 E011contadorPalabras.py

Proposito: Suponiendo que hemos introducido una cadena por teclado que representa una frase (palabras separadas por espacios),
           realiza un programa que cuente cuantas palabras tiene.


@author: Álvarez Fernández José Luis

Fecha : 26/10/2019

'''

'''
Variables:
cadena (cadena): almacenará la frase introducida por el usuario

Algoritmo:

LEER: cadena
CALCULAR: bucle while mientras introduzcamos una cadena haga:
          declaramos una variable llamada cambios a cero y otra llamada anterior como un espacio en blanco
          lo que haran estas dos variables es que contaran todos los cambios que se produzcan entre cada espacio
          y asi sabremos cuantas palabras hay, por cada espacio sabemos que hay 2 palabras
          condicional if para comprobar esto
          luego creamos otro condicional para comprobar que lac adena no acaba en un espacio que daria lugar a errar 
          en la suma de palabras
ESCRIBIR: palabras

'''
# Pedimos al usuario que introduzca los datos por pantalla

cadena = str(input("Introduce una frase: "))

# Calculos

while cadena != '':
    cambios = 0
    anterior = ' '
    for caracter in cadena:
        if caracter == ' ' and anterior != ' ':
            cambios += 1
        anterior = caracter

    if cadena[-1] == ' ':
        cambios -= 1
    palabras =  cambios + 1 

    # mostramos el resultado por pantalla
    #    
    print("El número total de palabras es de: ", palabras)

    cadena = str(input(" "))
