"""
1. Modifica el ejercicio 1 del tema anterior de manera que:

El programa admita dos parámetros:

    El primero es la ciudad de la que vamos a sacar el pronóstico de la temperatura,
    si la ciudad es errónea el programa termina con un mensaje de error y código 2.

    El segundo es opcional, y si existe, es el directorio donde vamos a crear un fichero html con la información formateada
    como una tabla del pronóstico de la temperatura, si no existe la información se muestra por pantalla.
    Consideraciones:
        este fichero tendrá por nombre: {CIUDAD}_{FECHA-INICIO}_{FECHA_FIN}, ejemplo: "Cordoba_2020-02-27-12.00.00_2020-03-03-09.00.00.html"
        si el fichero no se puede crear el programa termina con un mensaje de error y código 3.
        Si el programa no recibe ningún parámetro o recibe más de dos terminará con un mensaje de error (código 1) diciendo que la sintaxis es incorrecta.
        Si el programa recibe un solo parámetro y este es "-h" el programa muestra un texto explicando qué hace.
"""
def ayuda():
    return ("El programa nos mostrará el pronóstico de la temperatura de la ciudad introducida.\n"
            "- El primer parámetro será la ciudad de la cual queramos saber el pronóstico, indicando\n"
            "las dos primeras letras del país separado con una coma si la ciudad corresponde con\n"
            "otro pais.\n"
            "- El segundo parámetro será opcional y este será la ruta donde guardará el archivo\n"
            "html con los datos guardados. En caso de no añadir segundo parámetro los datos serán\n"
            "directamente mostrados por pantalla.")




if __name__ == '__main__':

    import sys
    import requests  # importamos requests para manejar peticiones http

    ciudad = ""
    directorio = ""
    ruta = "C:Users\AJFRU\Desktop\1º DAW 2019-2020\PROGRAMACION\PYTHON\pgn19-20\II_trimestre\excepciones"

    # Comprobamos parámetros
    if (len(sys.argv) == 2) or not (len(sys.argv == 3)):
        print("Introduce los parámetros correctamente")
        exit(2)
    if len(sys.argv) == 1:
        sys.argv[1] = ciudad
    if len(sys.argv) == 2:
        sys.argv[1] = ciudad
        sys.argv[2] = directorio

    # datos para hacer la peticion GET
    url = 'https://api.openweathermap.org/data/2.5/forecast'
    parametros = {'q': ciudad, 'units': 'metric', 'mode': 'json', 'APPID': 'f13188ece6f3d740bc6070c6c42acef0', 'lang': 'es'}

    # petición GET
    response = requests.get(url, params=parametros)
    if response.status_code != 200:
        print("Error al hacer la petición", response.status_code)
        exit(1)

    # resultados
    print("Petición URL:", response.url, "\n")
    print("Status Code:", response.status_code, "\n")

    # datos es un diccionario
    datos = response.json()

    # calculos
    dias = dict()  # diccionario con clave el dia y valor de medicinas del dia
    totales = list()  # lista de mediciones diarias
    for medicion in datos['list']:
        # fecha y temperatur medicion
        dia = medicion['dt_txt'][0:10]
        temperatura = float(medicion['main']['temp'])
        # si no tenemos datos de ese dia creamos una nueva entrada en el diccionario
        if not dias.get(dia):
            dias[dia] = list()
        # añadimos medicion
        dias[dia].append(temperatura)
        totales.append(temperatura)

    # resultados

    print()
    for dia, temps in dias.items():
        print(f"dia {dia[8:]}-{dia[5:7]}-{dia[0:4]}:\t Temperatura media: {(sum(temps) / len(temps)):.2f}º,minima {min(temps)}º y maxima: {max(temps)}º")

    print()
    print(f"Totales:\tTemperatura media: {(sum(totales) / len(totales)):.2f}º, Temperatura maxima: {max(totales)}º, Temperatura minima {min(totales)}º")
