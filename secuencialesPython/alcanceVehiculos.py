# Programa: Ejercicio16 alcanceVehiculos.py
#
# Proposito:  Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una distancia d. 
#             El que está detrás viaja a una velocidad mayor. 
#             Se pide hacer un algoritmo para ingresar la distancia entre los dos vehículos (km) y sus respectivas velocidades (km/h) 
#             y con esto determinar y mostrar en que tiempo (minutos) alcanzará el vehículo más rápido al otro.
# 
#
# @author: Álvarez Fernández José Luis
# Fecha : 10/10/2019
#
#
# Variables a usar
# vehiculo1 (numérica): almacenará la velocidad del vehiculo 1 
# vehiculo2 (numérica): almacenará la valocidad del vehiculo 2
# distancia (numérica): almacenará la distancia que separa a los dos vehiculos
# alcance (numérica): almacenará el tiempo que tardan en alcanzarse los vehiculos (distancia / (vehiculo1- vehiculo2)) *60;
# 
# 
#
#
# Algoritmo:
#
# LEER vehiculo1, vehiculo2, distancia
# CALCULAR alcance
# ESCRIBIR alcance


# Pedimos al usuario que introduzca los datos por pantalla
vehiculo1 = int(input("Introduce la velocidad del primer vehiculo: "))
vehiculo2 = int(input("Introduce la velocidad del segundo vehiculo (debe de ser mayor que la del primer vehiculo): "))
distancia = int(input("Introduce la distancia que separa a los vehiculos en km: "))


# Calculos

alcance = "{0:.0f}".format((distancia / (vehiculo2- vehiculo1)) *60) 

# Mostrar resultados por pantalla

print("El segundo vehiculo alcanzara al primer vehiculo en: ", alcance, " minutos")
