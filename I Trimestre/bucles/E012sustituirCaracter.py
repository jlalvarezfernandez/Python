'''
Programa: Ejercicio 12 E012sustituirCaracter.py

Proposito: Pide una cadena y dos caracteres por teclado (valida que sea un carácter), 
           sustituye la aparición del primer carácter en la cadena por el segundo carácter.


@author: Álvarez Fernández José Luis

Fecha : 26/10/2019

'''

'''
Variables:
cadena (cadena): almacenará la frase introducida
caracter1 (cadena): almacenará el primer caracter que queremos cambiar
caracter2 (cadena): almacenará el segundo caracter que queremos sutituir por el primer caracter

Algoritmo:
LEER: cadena, caracter1, caracter2
CALCULAR: bucle while para mostar que la longitud del caracter1 y del caracter2 sea de un solo caracter
          despues bucle while para mostrar que si caracter1 es diferente de caracter2 almacenara¡emos en la variable cambio 
          gracias al metodo replace el caracter1 popr el caracter2
ESCRIBIR: cambio


'''
# Pedimos al usuario que introduzca los datos por pantalla

cadena = str(input("Introduce una frase: "))
caracter1 = str(input("Introduce el primer caracter: "))
caracter2 = str(input("Introduce el segundo caracter: "))

# Calculos

while len(caracter1) != 1 or len(caracter2) != 1:
   
    if len(caracter1) == 1 and len(caracter2) == 1:
           print("continua con el ejercicio")

    else:
        print("ERROR, no has introducido un caracter: ")
        caracter1 = str(input("Introduce el primer caracter: "))
        caracter2 = str(input("Introduce el segundo caracter: "))

while caracter1 != caracter2:
    cambio = cadena.replace(caracter1,caracter2)

# Mostramos los resultados por pantalla

    print("La nueva frase sería: ",cambio)
    programa = int(input("programa finalizado"))



    



    