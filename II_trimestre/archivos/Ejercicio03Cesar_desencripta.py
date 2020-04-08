"""
PROPOSITO: 3. Haz un programa que reciba como parámetro un fichero encriptado con el método César y que almacene
              el resultado en otro, que también pasamos como parámetro, de manera que:

                Si el programa no recibe dos parámetros termina con un error 1.

                Si el programa recibe un solo parámetro guardará la información encriptada en el mismo archivo del que lee,
                pero antes advertirá al usuario de que machacará el archivo origen, dando opción a que la operación no se haga.

                Si el fichero origen no existe (da error al abrirlo como lectura) el programa termina
                con un mensaje de error y código 2.

                Si en el fichero destino no se puede escribir da error al abrirlo como lectura) el programa termina
                con un mensaje de error y código 2.

               Para desencriptar necesitas una clave que debes pedir al usuario.

              ¿Se te ocurre alguna forma de desencriptar este archivo sin pedir clave?
              Coméntala, y si te atreves... ¡impleméntala!
"""

import sys
import string

def desencripta_cesar(cadena, desplazamiento):
    """
        Desencripta la cadena recibida como parámetro.
        :param cadena:
        :param desplazamiento:
        :return: carácter encriptado
        """
    letras = string.ascii_letters + "áéíóúüñÁÉÍÓÚÜÑ"
    cadena_desencriptada = ""
    for caracter in cadena:
        # si el carácter es alfabético, encriptamos
        if caracter in letras:
            posicion_donde_esta = letras.index(caracter)
            posicion_caracter_desencriptado = (posicion_donde_esta - desplazamiento) % len(letras)
            if posicion_caracter_desencriptado < 0:
                posicion_caracter_desencriptado = len(letras) + posicion_caracter_desencriptado
            caracter = letras[posicion_caracter_desencriptado]
        # añadimos a la cadena encriptada
        cadena_desencriptada += caracter
    return cadena_desencriptada


if __name__ == '__main__':

    # Si el programa no recibe dos parámetros termina con un error 1.

    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Error, el programa no ha recibido 2 parámetros", file=sys.stderr)
        exit(1)

    # Si el programa recibe un solo parámetro guardará la información encriptada en el mismo archivo del que lee,
    # pero antes advertirá al usuario de que machacará el archivo origen, dando opción a que la operación no se haga

    fichero_origen = sys.argv[1]

    if len(sys.argv) == 2:
        fichero_destino = fichero_origen
        print("Este programa solo tiene un único parámetro, por lo que el archivo podría sobreescribirse")
        opcion = str(input("¿Desea sobreescribir la información en el mismo fichero (S/N) ?: "))
        while True:
            if opcion == "S" or opcion == "s":
                break
            elif opcion != "S" or opcion != "s":
                print("Operación cancelada")
                exit(4)
    else:
        fichero_destino = sys.argv[2]

    # Si el fichero origen no existe (da error al abrirlo como lectura) el programa termina con un mensaje de error y código 2.

    try:
        manejador_origen = open(fichero_origen, "r")
    except FileNotFoundError:
        print("Error el archivo no puede leerse", file=sys.stderr)
        exit(2)



    # tenemos que pedir el desplazamiento para poder ecriptar el archivo según el método Cesar
    while True:
        try:
            desplazamiento = int(input("Introduce el desplazamiento para la desencriptación según el método Cesar:"))
        except ValueError:
            print("Debes introducir un número entero")
        else:
            break

    # Si en el fichero destino no se puede escribir da error al abrirlo como lectura) el programa termina
    # con un mensaje de error y código 2.

    # leemos el archivo_origen y lo guarda en una lista
    origen = manejador_origen.readlines()
    # cerramos el archivo
    manejador_origen.close()

    try:
        manejador_destino = open(fichero_destino,"w")
    except PermissionError or FileNotFoundError:
        print("Error el archivo no puede escribirse", file=sys.stderr)
        exit(2)

    for i in origen:
        manejador_destino.write(desencripta_cesar(i, desplazamiento))
    manejador_destino.close()





