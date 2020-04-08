'''
Funciones matematicas para los ejercicios de Python

@author José Luis Álvarez Fernández

'''

'''
Aqui voy a ir haciendo las distintas funciones que necesito  para hacer los ejercicios

'''

'''
Creamos la función es_capicua:

Devuelve verdadero si el número que se pasa como parámetro es capicúa y falso en caso contrario.

- como parametro recibe un numero.
- ese numero entero lo convertimos a cadena.
- con un ciclo for recorremos esa cadena de atras hacia delante.
- creamos una variable para almacenar es número dado la vuelta.
- invertido le vamos concatenando los valores de i del ciclo for para tener el número al reves.
- devolvemos erdadero si cadnum (que seria el número convertido a cadena) es igual al invertido

'''

def es_capicua (numero):

    invertido = ""

    cad_num = str(numero)

    for i in range(len(cad_num),0,-1):

        invertido += cad_num[i]

    return (cad_num == (invertido))


'''
Creamos la función es_primo

Devuelve verdadero si el número que se pasa como parámetro es primo y falso en caso contrario.

- como parametros le pasamos un numero entero
- declaramos primo como verdadero ( empezaremos pensando que todos los números son primos).
- imcializamos la variable num a 2, porque comprobaremos desde ese numero
- bucle while mientras la raiz cuadrada del numero que estemos analizando sea menor que 2 y sea primo
  hacemos un condicional para saber si ese el resto de dividir ese numero entre 2 es 0 nos devuelva false (no es un numero primo)
- devolvera verdadero si es un número primo

'''


import math
def es_primo (numero):

    primo= True
    num = 2

    while num < math.sqrt(numero) and primo:
        if numero % num == 0:
            return False
        return True



'''
Creamos la funcion siguiente_primo: 

Devuelve el menor primo que es mayor al número que se pasa como parámetro.

- como parametro le vamos a pasar un número entero
- vamos a necesitar la funcion es_primo para comprobar si el número es primo
- con un buble while hacemos que mientras numero no sea primo incremente en uno el numero y vaya comprobandolo hasta encontrar 
  el numero primo
- en el caso de que sea primo el numero metido le incrementamos uno al numero para entrar en el bucle while

'''

def siguiente_primo (numero):

    num = numero +1

    while not es_primo(num):
        num+=1
    return num


'''
Creamos la función potencia: 

Dada una base y un exponente devuelve la potencia.

- como parametro le pasamos un número entero como base y otro como exponente
- creamos una variable que sera igual a la base
- hacemos un ciclo for que recorra el exponente tantas veces como se haya declarado
- el resultado lo multiplicamos por tantas veces como se recorra el exponente
- mostramos resultados



'''
def potencia (base,exponente):

    resultado = base

    for i in range(1,exponente,1):
        resultado *= base
    return resultado
'''

Creamos la función digitos:

Cuenta el número de dígitos de un número entero.

- como parametros le pasamos un numero entero
- pasamos el numero a cadena
- con un ciclo for recorremos la longitud de la cadena
- mostramos la longitud de la cadena


'''

def digitos (numero):

    cad_num = str(numero)

    for i in cad_num:
        return len(cad_num)


'''
creamos la funcion voltea: 

Le da la vuelta a un número.

- como parametros le pasamos un número entero
- creamos una variable para pasar el numero a una cadena
- primero comprobamos que si el numero introducido es un 0 devuelva 0
- despues creamos un bucle while, mientras el numero introducido sea mayor que 0
  calculamos su resto entre 10 y dividimos el número entre 10
- pasamos el resto concatenado a la variable que almacena la cadena
- devolvemos el numero volteado pasado a entero.

'''
def voltea(numero):
    num_volteado = " "
    if numero == 0:
        return 0

    while numero > 0:
        resto = numero % 10
        numero = numero // 10

        num_volteado += str(resto)

    return int(num_volteado)


'''
Creamos la función digitoN: 

Devuelve el dígito que está en la posición n de un número entero. Se empieza contando por el 0 y de izquierda a derecha.

- como parametros le pasamos dos enteros, uno para el numero y otro para ela posición del digito
- pasamos el numero a cadena
- creamos una variable para buscar la posicion deseada y lo pasamos a entero
- devolvemos la posicion del digito
'''

def digito_n(numero,posicion):

    cad_num = str(numero)

    posicion_digito = int(cad_num[posicion:posicion+1])


    return posicion_digito

'''
creamos la función posicionDeDigito: 

Da la posición de la primera ocurrencia de un dígito dentro de un número entero. Si no se encuentra, devuelve -1.

- como parametros pasamos 2 enteros, uno para el numero y otro para el digito
- pasamos el numero y el digito a buscar a cadena
- condicional si numero es mayor que 0 devuelve la posicion del digito
- si no devuelve -1

'''

def posicion_digito(numero, digito):

    cad_num = str(numero)

    cad_digito = str(digito)

    if numero > 0:
        return cad_num.index(cad_digito)
    else:
        return -1

'''
Creamos la función quitaPorDetras: 

Le quita a un número n dígitos por detrás (por la derecha).

- le pasamos como parametros un numero entero y otro para la cantidad de digitos a quitar
- pasamos el numero a cadena
- creamos una variable para quitar de la longitud de la cadena los digitos que queramos
- pasamos el numero de nuevo a entero
- devolvemos el numero

'''
def quita_por_detras (numero, cantidad_a_quitar):
    cad_num = str(numero)
    quitar_digitos = cad_num[0,len(cad_num)-cantidad_a_quitar]
    numero = int(quita_por_detras())
    return numero


'''
Creamos la función quitaPorDelante: 

Le quita a un número n dígitos por delante (por la izquierda).

- los parametros que le vamos a pasar van a ser un entero para el numero y otro para la cantidad de digitos a quitar
- pasamos el nuemro a cadena
- creamos una variable para quitar de la longitud d ela cadena la cantidad de numeros por la derecha elegidos
- pasamos el numero a entero de nuevo
- devolvemos el numero

'''

def quita_por_delante(numero,cantidad_a_quitar):
    cad_num = str(numero)
    quitar_digitos = cad_num[cantidad_a_quitar,len(cad_num)]
    numero = int(quitar_digitos)
    return numero



'''
Creamos la funcion pegaPorDetras: 

Añade un dígito a un número por detrás.

- los parametros que vamos a paserle a la función son el numero entero  y la cantidad a añadir
- pasamos el numero y la cantidad a cadena
- creamos una variable  nuevaq para concatenar los cadenas 
- pasamos esa variable a entero


'''

def pega_por_detras (numero,cantidad):

    cad_num = str(numero)
    cad_can = str(cantidad)

    num_pegados = (cad_num+ cad_can)
    numero = int(num_pegados)

    return numero


'''
Creamos la funcion pegaPorDelante: 

Añade un dígito a un número por delante.

- los parametros que vamos a paserle a la función son el numero entero  y la cantidad a añadir
- pasamos el numero y la cantidad a cadena
- creamos una variable  nueva para concatenar los cadenas 
- pasamos esa variable a entero


'''

def pega_por_delante (numero,cantidad):

    cad_num = str(numero)
    cad_can = str(cantidad)

    num_pegados = (cad_can + cad_num)
    numero = int(num_pegados)

    return numero


'''
creamos la funcion trozoDeNumero: 

Toma como parámetros las posiciones inicial y final dentro de un número y devuelve el trozo correspondiente.

- le pasamos como parametros tres enteros, uno para el numero, otro para la posicion inicial y otro para la posicion final
- pasamos el nuemro a cadena
- creamos una variable para guardar el trozo correspondiente
- lo pasamos a entero
- devolvemos los resultados
'''
def trozo_numero (numero,pos_ini,pos_final):
    cad_num = str(numero)
    trozo = cad_num[pos_ini,pos_final]
    numero = int(trozo)

    return numero

'''

creamos la funcion juntaNumeros: 

Pega dos números para formar uno.

- le pasamos como parametros 2 enteros
- pasamos el primer nuemro a cadena
- pasamos el segundo numero a cadena
- creamos una variable para concatenar lso numeros
- la pasamos a entero
- mostramos los resultados
- tambien podemos llamar a la funcion pega_por_delante que hace lo mismo



'''

def junta_numeros (numero1, numero2):

    return pega_por_delante(numero1,numero2)


#if __name__ == '__main__':
