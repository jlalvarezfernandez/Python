'''
Programa: Ejercicio 2 E02positivoNegativoCero.py

Proposito: Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir). 
           El programa debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.


@author: Álvarez Fernández José Luis

Fecha : 26/10/2019

'''
'''
variables:

cantidad (numérica): almacenará la cantidad de números introducidos por el usuario
contadorPos (numérica): contador de números positivos introducidos, se inicia en 0 porque no se ha introducido ninguno todavia
contadorNega (numérica): contador de números negativos introducidos, se inicia en 0 porque no se ha introducido ninguno todavia
contadorCeros (numérica): contador de ceros introducidos, se inicia en 0 porque no se ha introducido ninguno todavia
num (numérica): alamcenará los numeros introducidos ya sean positivos, negativos o cero

algoritmo:
LEER: cantidad
CALCULAR: ciclo for-in para introducir los números
          condicional if para los números positivos, con contador de números positivos introducidos
          elif para los núemros negativos, con su correspondiente contador de números negativos introducidos
          else para los números que sean cero con su correspondiente contador de números introducidos igual a cero
ESCRIBIR: contadorPos, contadorNega, contadorCeros


'''
# Pedimos al usuario que introduzca la información por pantalla

cantidad = int(input("Introduce una cantidad de números: "))

# Declaramos los contadores a cero para los números negativos, positivos y ceros

contadorPos = 0
contadorNega = 0
contadorCeros = 0

# Calculos

for cantidad in range(1,cantidad+1):
    num = int(input("Introduce un número: "))

    if num > 0:
        contadorPos += 1
    elif num < 0:
        contadorNega += 1
    else:
        contadorCeros += 1

# Mostramos los resutados por pantalla

print("Has introducido: ", contadorPos, " números positivos")
print("Has introducido: ", contadorNega, " números negativos")
print("Has introducido: ", contadorCeros, " ceros")
   

