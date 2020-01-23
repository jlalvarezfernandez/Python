# Programa: Ejercicio11 distanciaNumeros.py
#
# Proposito:  Pide al usuario dos números y muestra la "distancia" entre ellos 
#             (el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).
# 
#
# @author: Álvarez Fernández José Luis
# Fecha : 10/10/2019
#
#
# Variables a usar
# numero1 (númerica): almacenará el valor del primer número 
# numero2 (númerica): almacenará el valor del segundo número 
# distancia(númerica): almacenará la distancia que hay entre los números abs(numero1 - numero2) 
# 
#
# Algoritmo:
#
# LEER numero1, numero2
# CALCULAR distancia 
# ESCRIBIR distancia

#Pedimos al usuario que introduzca la informacion por pantalla

numero1 = float(input("Introduce el primer número: "))

numero2 = float(input("Introduce el segundo número: "))

#Calculos

distancia = abs(numero1 - numero2)

# Mostramos los resultados por pantalla

print ("La distancia entre ambos números es de: ", distancia)


