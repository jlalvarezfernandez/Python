# Programa: Ejercicio7 horasYMinutos.py
#
# Proposito: Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.
#
# @author: Álvarez Fernández José Luis
# Fecha : 10/10/2019
#
#
# Variables a usar
# minutos (númerica): almacenará la cantidad de minutos 
# horas (númerica): almacenará el número de horas a la que equivalen los minutos introducidos (minutos//60)
# restoMinutos (númerica): almacenará el número de minutos sobrantes a las horas (minutos%60)
#
# Algoritmo:
#
# LEER minutos
# CALCULAR horas, restoMinutos
# ESCRIBIR horas, restoMinutos

#Pedimos al usuario que introduzca los datos por pantalla

minutos = int(input("Introduce la cantidad de minutos que quieres convertir en horas y minutos: "))

#Operaciones

horas = minutos//60  # con la division entera obtenemos el número de horas

restoMinutos = minutos%60  # con el modulo obtenemos el resto de los minutos sobrantes

#Mostramos los resultados por pantalla

print("El numero de minutos introducidos equivale a: ", horas,  "horas y ", restoMinutos, " minutos")
