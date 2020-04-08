'''
Programa: Ejercicio 20 E20CompañiaTransporte.py

Proposito: Una compañía de transporte internacional tiene servicio en algunos países de 
           América del Norte, América Central, América del Sur, Europa y Asia. 
           El costo por el servicio de transporte se basa en el peso del paquete y la zona a la que va dirigido. 
           Lo anterior se muestra en la tabla:

                        ZONA	UBICACIÓN	COSTO/GRAMO
                            1	América del Norte	24.00 euros
                            2	América Central	20.00 euros
                            3	América del Sur	21.00 euros
                            4	Europa	10.00 euros
                            5	Asia	18.00 euros
            Parte de su política implica que los paquetes con un peso superior a 5 kg no son transportados, 
            esto por cuestiones de logística y de seguridad. 
            Realice un algoritmo para determinar el cobro por la entrega de un paquete o, en su caso, el rechazo de la entrega.



@author: Álvarez Fernández José Luis

Fecha : 17/10/2019
'''
'''
variables a usar:
peso (numérica): almacenará el peso en gramos del paquete a enviar
opcion (numérica): almacenará la zona de envio (dependiendo del pais elegido)
precio (numérica): almacenara el precio del envio (peso * preciogramo)


Algoritmo:

LEER: peso, opcion,    
CALCULAR: crear condicional if para introducir el peso del paquete
          crear menu con la opcion a elegir y realizar los calculos del precio
ESCRIBIR: precio
'''


# Pedimos al usuario que introduzca los datos por pantalla

peso = float(input("Introduce el peso del paquete en gramos: "))

# Calculos

if peso > 5000:
    print("Error, el envio no puede superar ese peso")
else:
    print("A continuacion saldran las diferentes zonas de envio")


    print("ZONA     UBICACIÓN     COSTO/GRAMO")
    print("-----------------------------------")
    print(" 1   América del Norte    24.00 euros")
    print(" 2   América Central      20.00 euros")
    print(" 3   América del Sur      21.00 euros")
    print(" 4   Europa               10.00 euros")
    print(" 5   Asia                 18.00 euros")

    opcion =int(input("Elige una zona del 1 al 5 para enviar tu paquete: "))


    if opcion == 1:
        precio = peso * 24
        print("Has elegido America del Norte y el precio a pagar por el envio será de: ",precio, " euros")
    elif opcion == 2:
        precio = peso * 20
        print("Has elegido America Central y el precio a pagar por el envio será de: ",precio, " euros")
    elif opcion == 3:
        precio = peso * 21
        print("Has elegido America del Sur y el precio a pagar por el envio será de: ",precio, " euros")
    elif opcion == 4:
        precio = peso * 10
        print("Has elegido Europa y el precio a pagar por el envio será de: ",precio, " euros")
    elif opcion == 5:
        precio = peso * 18
        print("Has elegido Asia y el precio a pagar por el envio será de: ",precio, " euros")
    else:
        print("Zona de envio incorrecta!!!!")








