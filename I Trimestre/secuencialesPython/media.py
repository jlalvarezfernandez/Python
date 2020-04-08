# Programa: Ejercicio6 media.py
#
# Proposito: Calcular la media de tres números pedidos por teclado.
#
# @author: Álvarez Fernández José Luis
# Fecha : 10/10/2019
#
#
# Variables a usar
# numero1 (númerica): almacenará el valor del primer número 
# numero2 (númerica): almacenará el valor del segundo número 
# numero3 (númerica): almacenará el valor del tercer número 
# media  (numérica): almacenara la media de los tres números(numero1 + numero2 + numero3) / 3 
#
# Algoritmo:
#
# LEER numero1, numero2, numero3
# CALCULAR media 
# ESCRIBIR media


#Pedimos al usuario que introduzca los datos por pantalla

numero1 = float(input("Introduce el primer numero: "))

numero2 = float(input("Introduce el segundo numero: "))

numero3 = float(input("Introduce el tercer numero: "))

#Operaciones

media = (numero1 + numero2 + numero3) / 3 

#Mostramos los resultados por pantalla

print("La media de los tres numeros introducidos es de: ", media)




