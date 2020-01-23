# Programa: Ejercicio18 mostrarIniciales.py
#
# Proposito:  Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.
# 
#
# @author: Álvarez Fernández José Luis
# Fecha : 10/10/2019
#
#
# Variables a usar
# nombre (cadena): almacenará el nombre 
# apellido1 (cadena): almacenará el primer apellido 
# apellido2 (cadena): almacenará el segundo apellido
# inicialNombre (cadena): almacenará la primera letra de tu nombre (nombre[0:1])
# inicialApellido1 (cadena): almacenará la primera letra de tu primer apellido (apellido1[0:1])
# inicialApellido2 (cadena): almacenará la primera letra de tu segundo apellido(apellido2[0:1])
#
#
# Algoritmo:
#
# LEER nombre, apellido1, apellido2
# CALCULAR inicialNombre, incialApellido1, incialApellido2 
# ESCRIBIR cuadrada, cubica


# Pedimos al usuario que introduzca los datos por pantalla

nombre = str(input("Introduce tu nombre: "))
apellido1 = str(input("Introduce tu primer apellido: "))
apellido2 = str(input("Introduce tu segundo apellido: "))

# Calculos

inicialNombre = nombre[0:1]
incialApellido1 = apellido1[0:1]
incialApellido2 = apellido2[0:1]

# Mostramos los resultados por pantalla

print("La inicial de tu nombre es: ", inicialNombre, " la inicial de tu primer apellido es: ", incialApellido1, " y la inicial de tu segundo apellido es: ",incialApellido2 )
