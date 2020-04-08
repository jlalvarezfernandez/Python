# Programa: Ejercicio2 perimetroArea.py
#
# Proposito: Calcular el perí­metro y área de un rectángulo dada su base y su altura.
#
#
# Fecha : 10/10/2019
#
#
# Variables a usar
# base (númerica): almacenará la base del rectangulo   
# altura (numérica): almacenará la altura del rectangulo
# area (numérica): almacenará el area del rectangulo (base * altura)
# perímetro (numérica): almacenará el perimetro del rectangulo ((base * 2) + (altura * 2))
#
# Algoritmo:
#
# LEER base, altura
# CALCULAR area, perimetro 
# ESCRIBIR area, perímetro






#Pedimos al usuario que introduzca los datos por pantalla

base = float(input("Introduce el valor de la base del rectangulo: "))

altura =  float(input("Introduce el valor de la altura del rectangulo: "))

# Calculos

area = base * altura

perimetro = ((base * 2) + (altura * 2))


#Mostramos los resultados por pantalla

print("El área del rectangulo dados tus datos es de: ", area, "cm  y el perimetro es de: ", perimetro, " cm")
