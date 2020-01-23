# Programa: Ejercicio14 numeroInvertido.py
#
# Proposito:  Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido.
# 
#
# @author: Álvarez Fernández José Luis
# Fecha : 10/10/2019
#
#
# Variables a usar
# numero (númerica): almacenará el valor del número introducido 
# primeraCifra(numérica): almacenará el resultado del modulo de la división del número entre 10  (primeraCifra = numero%10)
# segundaCifra (numérica): almacenará el resultado de la division entera del número entre 10( segundaCifra = numero//10)
# numeroInvertido (numérica): alamcenará la suma de la primera cifra multiplicada por 10 mas la segunda cifra (primeraCifra*10 + segundaCifra)
#
# Algoritmo:
#
# LEER numero
# CALCULAR primeraCifra, segundaCifra, numeroInvertido
# ESCRIBIR numeroInvertido


# Pedimos al usuario que introduzca los datos por pantalla

numero = int(input("Introduce un número de dos cifras: "))

# Calculos

primeraCifra = numero%10

segundaCifra = numero//10

numeroInvertido = (primeraCifra*10 + segundaCifra)



# Mostramso el resultado por pantalla

print(numero, "invertido es: ", numeroInvertido) 
