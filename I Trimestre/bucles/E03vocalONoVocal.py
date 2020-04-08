'''
Programa: Ejercicio 3 E03vocalONoVocal.py

Proposito: Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ 
           en caso contrario, el programa termina cuando se introduce un espacio.


@author: Álvarez Fernández José Luis

Fecha : 26/10/2019

'''

'''
variables:

letra (cadena): almacenará la letra introducida

Algoritmo:

LEER: letra
CALCULAR: bucle while que si no se introduce un espacio por teclado realiza las sigueintes operaciones:
          if con las vocales, si lo cumple será una vocal
          else, si no lo cumple será una consonante
          el bucle se repetira hasta que introduzcamos un espacio por teclado

'''

# Pedimos al usuario que introduzca la información por pantalla

letra = str(input("Introduce una letra: "))

# Calculos

while letra != " ":
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        print("vocal")
    else:
        print ("no vocal")
    letra = str(input("Introduce una letra: "))
    
print ("Programa terminado")