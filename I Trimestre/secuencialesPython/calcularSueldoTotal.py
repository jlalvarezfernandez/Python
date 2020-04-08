# Programa: Ejercicio8 calcularSueldoTotal.py
#
# Proposito: Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, 
#            el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes 
#            y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.
#
# @author: Álvarez Fernández José Luis
# Fecha : 10/10/2019
#
#
# Variables a usar
# sueldoBase (númerica): almacenará el sueldo bae del trabajador 
# venta1 (númerica): almacenará el valor de la primera venta.
# venta2 (númerica): almacenará el valor de la segunda venta.
# venta3 (númerica): almacenará el valor de la tercera venta.
# comision (númerica): almacenará el valor de las ganancias por las tres ventas del trabajador (venta1 + venta2 + venta3) * 0.10
# sueldoTotal (numérica): almacenará la ganancia total mensiual del trabajador (sueldoBase + comision)
#
# Algoritmo:
#
# LEER sueldoBase, venta1, venta2, venta3
# CALCULAR comision, sueldoTotal
# ESCRIBIR sueldoTotal


#Pedimos al usuario que introduzca los datos por pantalla

sueldoBase = float(input("Introduce el sueldo base del trabajador: "))

venta1 = float(input("Introduce el valor de la primera venta: "))

venta2 = float(input("Introduce el valor de la segunda venta: "))

venta3 = float(input("Introduce el valor de la tercera venta: "))


#Operaciones

comision = (venta1 + venta2 + venta3) * 0.10
sueldoTotal = sueldoBase + comision

#Mostramos los resultados por pantalla

print("El sueldo total del trabajador será de: ", sueldoTotal, " euros")

