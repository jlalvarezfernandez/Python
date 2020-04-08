# Programa: Ejercicio15  intercambioValores.py
#
# Proposito:  Dadas dos variables numéricas A y B, que el usuario debe teclear, 
#             se pide realizar un algoritmo que intercambie los valores de ambas variables y muestre cuanto valen al final las dos variables.
# 
#
# @author: Álvarez Fernández José Luis
# Fecha : 10/10/2019
#
#
# Variables a usar
# numero1 (númerica): almacenará el valor del primer número introducido 
# numero2 (númerica): almacenará el valor del segundo número introducido 
# cambio (numérica): almacenará el valor del primer número en ella
# numero1 (numérica): ahora lamacenara el valor del segundo número
# numero2 (numérica) ahora lamacenara el valor de cambio
#
# Algoritmo:
#
# LEER numero1, nuemro2
# CALCULAR cambio, numero1, nuemro2
# ESCRIBIR numero1, numero2


# Pedimos al usuario que introduzca los datos por pantalla

numero1 = float(input("Introduce el valor de la variable numérica 'A': "))
numero2 = float(input("Introduce el valor de la variable numérica 'B': "))

# Calculos

cambio = numero1
numero1 = numero2
numero2 = cambio



# Mostramos los resultados por pantalla

print("El valor numerico de 'A' ahora es: ", numero1,  " y el valor numérico de 'B' ahora es: ", numero2)

