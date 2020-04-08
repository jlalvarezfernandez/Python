"""
PROPOSITO:   2. Crea un programa que encripte un fichero que le pasamos como parámetro y almacene el resultado en otro,
                que también pasamos como parámetro, de manera que:

                    -Si el programa no recibe dos parámetros termina con un error 1.

                    Si el programa recibe un solo parámetro guardará la información encriptada en el mismo archivo del
                    que lee, pero antes advertirá al usuario de que machacará el archivo origen,
                    dando opción a que la operación no se haga.

                    Si el fichero origen no existe (da error al abrirlo como lectura) el programa termina con un mensaje
                    de error y código 2.

                    Si en el fichero destino no se puede escribir (da error al abrirlo como lectura) el programa termina
                    con un mensaje de error y código 2.

                Para encriptar usa el método César, necesitarás una clave que debes pedir al usuario.
"""
import sys
import string

def encripta_cesar(cadena, desplazamiento):
    """
    Encripta la cadena recibida como parámetro.
    :param cadena:
    :param desplazamiento:
    :return: carácter encriptado
    """
    letras = string.ascii_letters + "áéíóúüñÁÉÍÓÚÜÑ"
    cadena_encriptada = ""
    for caracter in cadena:
        # si el carácter es alfabético, encriptamos
        if caracter in letras:
            posicion_donde_esta = letras.index(caracter)
            posicion_caracter_encriptado = (posicion_donde_esta + desplazamiento) % len(letras)
            caracter_encriptado = letras[posicion_caracter_encriptado]
        else:
            caracter_encriptado = caracter
        # añadimos a la cadena encriptada
        cadena_encriptada += caracter_encriptado
    return cadena_encriptada



if __name__ == '__main__':


    # Si el programa no recibe dos parámetros termina con un error 1.

    """
    En la posicion 1 se guarda el programa en la posición 0
    En la posicion 2 se guarda el primer parámetro (fichero_origen) en la posición 1
    En la posicion 3 se guarda el segundo parámetro (fichero_destino) en la posición 2
    por lo que tenemos 3 parámetros, 2 archivos y 3 posiciones
    
    """

    if (len(sys.argv) < 2 or len(sys.argv) > 3):
        # file=sys.stderr manda el mensaje a la salida de error stderr
        print("Error en el número de parámetros", file=sys.stderr)
        exit(1)

    # Si el programa recibe un solo parámetro guardará la información encriptada en el mismo archivo del
    # que lee, pero antes advertirá al usuario de que machacará el archivo origen, dando opción a que la operación no se haga.

    archivo_origen = sys.argv[1] # variable que va a estar en el parámetro 2, posicion 1

    if (len(sys.argv) == 2):
        archivo_destino = archivo_origen # porque solo existe un solo parámetro y el mismo archivo de origen sera el de
                                         # destino
        print("El archivo donde va a escribir es el mismo que usted tiene.")
        while True:
            opcion = str(input("¿Desea machacar la información del fichero (S/N) ?: "))
            if opcion == "S" or opcion == "s":
                break
            elif opcion != "S" or opcion != "s":
                print("Operación cancelada")
                exit(3)
    else:
        archivo_destino = sys.argv[2]

    # Ahora tenemos que leer el fichero origen, para ello lo guardamos en una lista para después poder procesarlo
    # Si el fichero origen no existe (da error al abrirlo como lectura) el programa termina con un mensaje de error y código 2.
    # esto la vamos a hacer con una excepcion
    try:  # ¿existe el fichero?
        manejador_origen = open(archivo_origen, "r")
    except FileNotFoundError:
        print("No se ha podido abrir", archivo_origen)
        exit(2)

        # tenemos que pedir el desplazamiento para poder ecriptar el archivo según el método Cesar
    while True:
        try:
            desplazamiento = int(input("Introduce el desplazamiento para la encriptación según el método Cesar:"))
        except ValueError:
            print("Debes introducir un número entero")
        else:
            break

    # leemos el archivo_origen y lo guarda en una lista
    origen = manejador_origen.readlines()
    manejador_origen.close()

    # ahora tenemos que escribir elfichero encriptado
    # Si en el fichero destino no se puede escribir (da error al abrirlo como lectura) el programa termina
    # con un mensaje de error y código 2.
    # volvemos a hacerlo con excepciones


    try:
        manejador_destino = open(archivo_destino, 'w')
    except PermissionError or FileNotFoundError:
        print("El fichero no se ha podido abrir para escritura")
        exit(2)


    # Después de hacer esto tenemos que recorrer todas las lineas del archivo origen y escribirlas en el manejador de destino

    for i in origen:
        manejador_destino.write(encripta_cesar(i, desplazamiento))
    manejador_destino.close()


