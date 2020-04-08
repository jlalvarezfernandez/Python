# Programa: Ejercicio9 PrecioConDescuento.py
#
# Proposito: Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto deberá pagar finalmente por su compra.
#
# @author: Álvarez Fernández José Luis
# Fecha : 10/10/2019
#
#
# Variables a usar
# precioInicial (númerica): almacenará el precio inicial sin descuento del producto 
# descuento (númerica): almacenará el descuento aplicado al producto (precioInicial * 0.15)
# precioFinal (númerica): almacenará el precio con descuento del producto (precioInicial - descuento)
# 
#
# Algoritmo:
#
# LEER precioInicial, desceunto, precioFinal venta1, venta2, venta3, 
# CALCULAR comision, sueldoTotal
# ESCRIBIR sueldoTotal

#Pedimos al usuario que introduzca la información por pantalla

precioInicial = float(input("Introduce el precio inicial del producto: "))

#Operaciones

descuento = precioInicial * 0.15
precioFinal = precioInicial - descuento

#Mostramos los resultados por pantalla

print("El precio final del articulo tras aplicar el descuento es de: ", precioFinal, " euros")
