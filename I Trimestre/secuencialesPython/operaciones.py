# Programa: Ejercicio4 operaciones.py
#
# Proposito: Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.
#
# @author: Álvarez Fernández José Luis
# Fecha : 10/10/2019
#
#
# Variables a usar
# numero1 (númerica): almacenará el valor del primer número
# numero2 (numérica): almacenará el valor del segundo número
# suma (numérica): almacenará el valor de la suma (numero1 + numero2)
# resta (numérica): almacenará el valor de la resta (numero1 - numero2)
# division (numérica): almacenará el valor de la división (numero1 / numero2)
# multiplicación (numérica): almacenará el valor de la multiplicación (numero1 * numero2)
#
# Algoritmo:
#
# LEER numero1, numero2
# CALCULAR suma, resta, división, multiplicación 
# ESCRIBIR suma, resta, división, multiplicación 

#Pedimos al usuario que introduzca los datos por pantalla

numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))

#Operaciones

suma = numero1 + numero2
resta = numero1 - numero2
division = "{0:.2f}".format(numero1 / numero2)
multiplicacion = numero1 * numero2

# Mostramos los resultados por pantalla

print("El resultado de sumar los dos numeros es de: " , suma)
print("El resultado de restar los dos numeros es de: " , resta)
print("El resultado de dividir los dos numeros es de: " , division)
print("El resultado de multiplicar los dos numeros es de: " , multiplicacion)

