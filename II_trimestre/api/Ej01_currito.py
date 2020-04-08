"""
1. Modifica el ejercicio 1 del tema anterior de manera que:

- El programa admita dos parámetros:
    - El primero es la ciudad de la que vamos a sacar el pronóstico de la temperatura, si la
ciudad es errónea el programa termina con un mensaje de error y código 2.
    - El segundo es opcional, y si existe es el directorio donde vamos a crear un fichero
html con la información formateada como una tabla del pronóstico de la temperatura, si
no existe la información se muestra por pantalla. Consideraciones:
        - este fichero tendrá por nombre: {CIUDAD}_{FECHA-INICIO}_{FECHA_FIN},
ejemplo: "Cordoba_2020-02-27-12:00:00_2020-03-03-09:00:00.html"
        - si el fichero no se puede crear el programa termina con un mensaje de error y código 3.
    - Si el programa no recibe ningún parámetro o recibe más de dos terminará con un mensaje de
error (código 1) diciendo que la sintaxis es incorrecta.
    - Si el programa recibe un solo parámetro y este es "-h" el programa muestra un texto
explicando qué hace.
"""
import requests, sys, os

ciudad = ""
URL_BASE = "https://api.openweathermap.org/data/2.5/forecast?"
ARGS = {'q': ciudad, 'appid': '7244cf3744b6759cb242a1dda9702905', 'lang': 'es', 'units': 'metric'}
ruta = ""


class parameter_error(Exception):
    """
    :exception Esta excepción es capturada cuando la ciudad vale 0 o cuando el estado
    de la petición no es 200.
    """
    def __init__(self, ciudad):
        Exception.__init__(self)
        self.ciudad = ciudad


class request_error(Exception):
    """
    :exception Esta excepción captura error en la petición
    """
    def __init__(self):
        Exception.__init__(self)
        self.ciudad = ciudad


def peticion(ciudad):
    """
    Método que hará petición get a la API
    :param ciudad:
    :return:
    """

    URL_BASE = "https://api.openweathermap.org/data/2.5/forecast?"
    ARGS = {'q': ciudad, 'appid': '7244cf3744b6759cb242a1dda9702905', 'lang': 'es', 'units': 'metric'}

    try:
        response = requests.get(url=URL_BASE, params=ARGS)
        #if response.status_code == 200:
            #return response.json()
        if ciudad == "-h":
            ayuda()
        elif ciudad == "":
            raise parameter_error(ciudad)
        elif response.status_code != 200:
            raise request_error
        else:
            datos = response.json()
            return datos

    except parameter_error:
        print("No se encuentra la ciudad")
        exit(1)

    except request_error():
        print("Error en la petición")
        exit(2)

def mostrar_html(ciudad):

    peticion(ciudad)
    #for medicion in peticion(ciudad)['list']:

    nombre_archivo = ciudad + "_" + peticion(ciudad)['list'][0]['dt_txt'] + "_" + peticion(ciudad)['list'][39]['dt_txt'] + ".html"
        # nombre_archivo = (medicion['city']['name']) + "_" + (medicion['list']['0']['main']['dt_txt']) + "_" + (medicion['list']['39']['main']['dt_txt']) + ".html"
    return nombre_archivo.replace(":",".").replace(" ","_")


def ayuda():
    """
    :return: Devuelve información del programa.
    """
    return ("El programa nos mostrará el pronóstico de la temperatura de la ciudad introducida.\n"
            "- El primer parámetro será la ciudad de la cual queramos saber el pronóstico, indicando\n"
            "las dos primeras letras del país separado con una coma si la ciudad corresponde con\n"
            "otro pais.\n"
            "- El segundo parámetro será opcional y este será la ruta donde guardará el archivo\n"
            "html con los datos guardados. En caso de no añadir segundo parámetro los datos serán\n"
            "directamente mostrados por pantalla."
            )

if __name__ == '__main__':

    ciudad = ""
    # Comprobamos parámetros
    try:
        if len(sys.argv) == 2:
            ciudad = sys.argv[1]
            mostrar_html(ciudad)
        elif len(sys.argv) == 3:
            ciudad = sys.argv[1]
            ruta = sys.argv[2]
            mostrar_html(ciudad)

    except parameter_error:
        print("Los parámetros no son correctos.")
        exit(1)     # Programa recibe mas de dos parametros termina con código 1.

    print(mostrar_html(ciudad))


