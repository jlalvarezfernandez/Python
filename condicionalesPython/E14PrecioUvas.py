'''
Programa: Ejercicio 14 E14PrecioUvas.py

Proposito: La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva,
           la cual se clasifica en tipos A y B, y además en tamaños 1 y 2.
           Cuando se realiza la venta del producto, ésta es de un solo tipo y tamaño,
           se requiere determinar cuánto recibirá un productor por la uva que entrega en un embarque,
           considerando lo siguiente: 
           si es de tipo A, se le cargan 20 céntimos al precio inicial cuando es de tamaño 1; y 30 céntimos si es de tamaño 2. 
           Si es de tipo B, se rebajan 30 céntimos cuando es de tamaño 1, y 50 céntimos cuando es de tamaño 2.
           Realice un algoritmo para determinar la ganancia obtenida.


@author: Álvarez Fernández José Luis

Fecha : 17/10/2019
'''
'''
variables a usar:
kilos (numérica): almacenará la cantidad d ekilos vendidos
precio (numérica): almacenará el precio de cada kilo de uva
tipo (numérica): almacenará el tipo de cada uva (A o B)
tamanio (numérica): almacenará el tamaño de las uvas (1 o 2)
precioFinal (numérica): alamcenará el precio final de las uvas(precio mas incremento o decremento)
ganancia (numérica): alamcenará el precioFinal * kilos vendidos


Algoritmo:

LEER: kilos, precio, tipo, tamanio 
CALCULAR: calcular las diferentes opciones de tipo y tamaño de uva
          calcular el precio final en funcion de los datos introducidos
ESCRIBIR: ganancia
'''

# Pedimos al usuario que introduzca los datos por pantalla

kilos = float(input("Introduce los kilos de uvas vendidos: "))
precio = float(input("Introduce el precio del kilo de uvas: "))
tipo = str(input("Introduce el tipo de uva ('A' o 'B'): "))
tamanio = int(input("Introduce el tamaño de la uva ( 1 o 2): "))

# Calculos

if tipo == 'A' or tipo == 'a':
    if tamanio == 1:
        precioFinal = precio + 0.20
    if tamanio == 2:
        precioFinal = precio + 0.30 
elif tipo == 'B' or tipo == 'b':
    if tamanio == 1:
        precioFinal = precio - 0.30 
    if tamanio == 2:
        precioFinal = precio - 0.50 
ganancia = precioFinal * kilos
# Mostramos los resultados por pantalla

print("La ganancia del vinicultor será de: ",ganancia, "euros")