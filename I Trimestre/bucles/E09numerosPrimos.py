'''
Programa: Ejercicio 9 E09numerosPrimos.py

Proposito: Mostrar en pantalla los N primero número primos. 
           Se pide por teclado la cantidad de números primos que queremos mostrar.




@author: Álvarez Fernández José Luis

Fecha : 26/10/2019

'''
'''
cantidad = int(input("Introduce la cantidad de números primos que quieres ver: "))

for i in range (2,cantidad):
    contador = 2
    primo = True
    while primo and contador <i:
        if i % contador == 0:
            primo = False
        else:
            contador +=1
    if primo == True:
        print("Estos son los ",cantidad,"primeros números primos", i)
'''


