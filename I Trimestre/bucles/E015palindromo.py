'''
Programa: Ejercicio 15 E015palindromo.py

Proposito: Introducir una cadena de caracteres e indicar si es un palíndromo. 
           Una palabra palíndroma es aquella que se lee igual adelante que atrás.



@author: Álvarez Fernández José Luis

Fecha : 26/10/2019

'''

'''
Variables:
cadena (cadena): almacenará la frase que introducirá el usuario por pantalla

Algoritmo:
LEER: cadena
CALCULAR: bucle while, mientras no se introduzca una cadena vacia se quitaran los espacios para poder usar mejor la cadena
          condicional para comprobar que todos los caracteres esten escritos en minusculas con islower.
          declaramos la variable inertida que almacenar ala cadena al reves sin espacios
          si la cadena invertida es igual a la introducida sin espacios serña palindroma sino no.
'''
# Pedimos al usuario que introduzca los datos por pantalla

cadena = str(input("Introduce una frase para saber si es un palíndromo:"))

# Calculos

while cadena != " ":
    sinEspacios = cadena.replace(" ","")
    if sinEspacios.islower() == False:
        sinEspacios = sinEspacios.lower() 
    invertida = sinEspacios[::-1]
    if invertida == sinEspacios:
        print("La frase es palindroma")
    else:
        print("la frase no es palindroma")

    cadena = str(input("programa terminado"))
    break

  
    

 

