'''
Programa: Ejercicio 5 E05limiteNumeros.py

Proposito: Escribe un programa que pida el limite inferior y superior de un intervalo.
           Si el límite inferior es mayor que el superior lo tiene que volver a pedir. 
           
           A continuación se van introduciendo números hasta que introduzcamos el 0. 
           Cuando termine el programa dará las siguientes informaciones:

                La suma de los números que están dentro del intervalo (intervalo abierto).
                Cuantos números están fuera del intervalo.
                Informa si hemos introducido algún número igual a los límites del intervalo.


@author: Álvarez Fernández José Luis

Fecha : 26/10/2019

'''

'''
Variables:

limInferior (numérica): almacenará el número que corresponde al limite inferior
limSuperior (numérica): almacenará el número que corresponde al limite superior

Algoritmo:

LEER: limInferior, limSuperior
CALCULAR: primero comprobamos que el limiteinferior es menor que el limite superior con un bucle while
          que pedira números hasta que introduzcamos correctamente los datos
          despues creamos una serie de contadores qie incrementarán las distintas operaciones que realizaremos con dichos números
          creamos un bucle while para comprobar que los numeros introducidos no son cero( se acabará al escribir cero)
          y hacemos varios condicionales para calcular la suma de los numeros dentro del intervalo, los que estan fuera del intervalo
          por ultimo los que sin igual que los limites, con otro condicional
ESCRIBIR: suma, fueraIntervalo


'''
# Pedimos al usuario que introduzca los datos por pantalla

limInferior = int(input("Introduce el primer número: "))
limSuperior = int(input("Introduce el segundo número: "))

# Calculos

while limInferior > limSuperior:
    print("vuelve a introducir los datos, el primer número debe ser inferior al segundo número.")
    limInferior = int(input("Introduce el primer número: "))
    limSuperior = int(input("Introduce el segundo número: "))

numero = int
suma = 0
fueraIntervalo = 0
igualLimites = False

while numero != 0:
    numero = int(input("Introduce números: (pulsa 0 para salir del programa y mostrar los resultados) "))
    if numero > limInferior and numero < limSuperior:
        suma += numero
    else:
        fueraIntervalo +=1 
    if numero == limInferior or numero == limSuperior:
        igualLimites == True


# Mostramos los resultados por pantalla        
print("La suma de los números dentro del intervalo es de: ",suma)
print("Has introducido: ",fueraIntervalo,"números fuera del intervalo")
if numero == igualLimites:
    print("Has introducido algún número igual que los limites")
else:
    print("No has introducido algún número igual que los limites")








