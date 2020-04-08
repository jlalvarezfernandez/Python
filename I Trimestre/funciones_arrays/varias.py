'''
Funciones para los ejercicios de arrays

    Creación de los ejercicos de funciones de arrays

    1. generaArrayInt: Genera un array de tamaño n con números aleatorios cuyo intervalo (mínimo y máximo) se indica como parámetro.

    2. minimoArrayInt: Devuelve el mínimo del array que se pasa como parámetro.

    3. maximoArrayInt: Devuelve el máximo del array que se pasa como parámetro.

    4. mediaArrayInt: Devuelve la media del array que se pasa como parámetro.

    5. estaEnArrayInt: Dice si un número está o no dentro de un array.

    6. posicionEnArray: Busca un número en un array y devuelve la posición (el índice) en la que se encuentra.

    7. volteaArrayInt: Le da la vuelta a un array.

    8. rotaDerechaArrayInt: Rota n posiciones a la derecha los números de un array.

    9. rotaIzquierdaArrayInt: Rota n posiciones a la izquierda los números de un array.


@José Luis Álvarez Fernández

'''
import random
import sys

'''
Creamos la función mostrar array que nos va a servir para mostar los arrays que creemos
'''


def mostrar_array(array):
    for i in array:
        print(i, end=" | ")


'''
Creamos la función generaArrayInt: 
Genera un array de tamaño n con números aleatorios cuyo intervalo (mínimo y máximo) se indica como parámetro.

'''


def genera_array_int(tamamnio, num_min, num_max):
    array = []

    for i in range(0, tamamnio):
        array.append(random.randint(num_min, num_max))

    return array


'''
Creamos la función minimoArrayInt

Devuelve el mínimo del array que se pasa como parámetro.

'''


def minimo_array_int(array):
    minimo = sys.maxsize
    for i in array:
        if i < minimo:
            minimo = i

    return minimo


'''

Creamos la función maximoArrayInt: 

Devuelve el máximo del array que se pasa como parámetro.

'''

def maximo_array_int(array):
    maximo = -sys.maxsize
    for i in array:
        if i > maximo:
            maximo = i
    return maximo

'''
Creamos la función mediaArrayInt: 

Devuelve la media del array que se pasa como parámetro.

'''

def media_array_int (array):
    media = 0
    for i in array:
        media += i/len(array)

    return media

'''
Creamos la función estaEnArrayInt: 

Dice si un número está o no dentro de un array.
'''

def esta_en_array_int (array,numero):
    if (numero in array):
        return True
    else:
        return False

'''
Creamos la función posicionEnArray: 

Busca un número en un array y devuelve la posición (el índice) en la que se encuentra.
'''

def posicion_en_array (array, numero):

    posicion = array.index(numero)

    return posicion

'''
Creamos la función volteaArrayInt: 

Le da la vuelta a un array.
'''

def voltea_array ():

    array.reverse()

    return array

'''
Creamos la función rotaDerechaArrayInt: 

Rota n posiciones a la derecha los números de un array.
'''
def rota_derecha_array (array, num_rotar):
    copia = [None] * len(array)
    c = num_rotar
    for i in range(len(array)):
        copia[c] = array[i]
        c += 1
        if c == len(array):
            c = 0
    for i in range(len(array)):
        array[i] = copia[i]

'''
Creamos la función rotaIzquierdaArrayInt: 
Rota n posiciones a la izquierda los números de un array.
'''
def rota_izquierda_array(array, n):
    copia = [None] * len(array)
    c = n
    for i in range(len(array),0):
        copia[c] = array[i]
        c += 1
        if c == 0:
            c = len(array)
    for i in range(len(array),0):
        array[i] = copia[i]


if __name__ == '__main__':
    # Generamos array aleatorio

    tamanio = int(input("Introduce el tamaño del array: "))

    num_min = int(input("Introduce el número mínimo del array: "))

    num_max = int(input("Introduce el numero máximo del array: "))

    array = genera_array_int(tamanio,num_min,num_max)

    print()

    mostrar_array(array)

    print()


    print("El valor mínimo es: ", minimo_array_int(array))

    print()

    print("El valor máximo es: ", maximo_array_int(array))

    print()

    print("La media de los número del array es: " ,media_array_int(array))

    print()

    numero= int(input("Introduce un número para saber si esta en el array: "))

    print("Esta el numero: ",esta_en_array_int(array,numero))

    print()

    posicion = int(input("Introduce la un número para saber su posición: "))

    if posicion in array:
        print("Esta es la posición: ",posicion_en_array(array,posicion))
    else:
        print("El número no se encuentra")

    print()

    print("Este es el array dado la vuelta", voltea_array())

    posicion_rotar = int(input("Introduce el nuemro de posiciones a rotar a la derecha: "))

    rota_derecha_array(array, posicion_rotar)
    print("Este es el array ahora rotado hacia la derecha: ", array)

    print()

    rotar_izquierda = int(input("Introduce el numero de posiciones a rotar a la izquierda: "))

    rota_izquierda_array(array,rotar_izquierda)

    print("Este es el array ahora rotado hacia la izquierda: ", array)




