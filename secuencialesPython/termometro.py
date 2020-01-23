# Programa: Ejercicio5 termometro.py
#
# Proposito: Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.
#
# @author: Álvarez Fernández José Luis
# Fecha : 10/10/2019
#
#
# Variables a usar
# farenheit (númerica): almacenará los grados farenheit 
# centigrados (numérica): almacenará los grados celsius (farenheit - 32 / 1.8000)
#
# Algoritmo:
#
# LEER farenheit
# CALCULAR centigrados 
# ESCRIBIR centigrados


#Pedimos al usuario que introduzca los datos por pantalla

farenheit = float(input("Introduce la cantidad de grados Farenheit que deseas convertir a grados celsius: "))

#Operaciones

centigrados = farenheit - 32 / 1.8000

#Mostramos los resultados por pantalla

print (farenheit, "grados Farenheit, equivalen a: ", centigrados, "grados celsius")
