"""
2. Haz un programa en Python que añada películas a un archivo de texto con el siguiente formato:
    • Una línea por cada película.
    • <TÍTULO>|<TÍTULO ORIGINAL>|<POPULARIDAD>|<VALORACIÓN>|<FECHA DE ESTRENO>

    --Este programa recibe como parámetro el nombre de una película (ponlo entre comillas para quePython sepa que es un
      único parámetro) y el fichero de texto donde añadirla.

    -Si el fichero no existe lo crea, si no puede da error.

    --Si el número de parámetros es incorrecto el programa da un error.

    Busca la película mediante API REST en https://developers.themoviedb.org/3/search/search-movies
    Si la película no está en el fichero la añade, si está muestra un mensaje diciendo que ya está en el
    archivo y no la añade.

    --En cualquier caso muestra por la pantalla el argumento de la película

    @author JOSÉ LUIS ÁLVAREZ FERNÁNDEZ
"""
import sys

import requests

# si el numero de parámetros es incorrecto el programa termina con un mensaje de error
if len(sys.argv) != 3:
    # file=sys.stderr manda el mensaje a la salida de error stderr
    print("Error en el número de parámetros", file=sys.stderr)
    exit(1)

# asignamos variables a los parámetros
nombre_pelicula = sys.argv[1]  # asignamos al parámetro 1 esta variable
fichero_txt = sys.argv[2]  # asignamos al parámetro 2 el nombre del fichero

# datos para hacer la petición
url = "https://api.themoviedb.org/3/search/movie"  # url utilizada
api_key = '242f6331a4ccccac0111863d092cbdbf'  # clave api
parametros = {'api_key': api_key, 'query': nombre_pelicula, 'language': 'es-ES'}

# hacemos la petición get

response = requests.get(url=url, params=parametros)

if response.status_code != 200:
    print("Error al hacer la petición", file=sys.stderr)
    exit(3)
else:
    print("Petición correcta")
    print("Url usada: ", url)
    print("Código de salida ==>", response.status_code)

# guardamos la información devuelta en un diccioanrio en formato json
datos = response.json()

print("Nombre de la pelicula buscada:", nombre_pelicula.upper())
print("Si hay mas de una coincidencia el programa devolverá error:")
print("---------------------------------------------------------------")

# si hay mas de una coincidencia del nombre de la pelicula da error
if datos['total_results'] > 1:
    print("Error, hay mas de una pelicula con ese titulo", file=sys.stderr)
    exit(4)

titulo = datos['results'][0]['title']
titulo_original = datos['results'][0]['original_title']
popularidad = datos['results'][0]['popularity']
valoracion = datos['results'][0]['vote_average']
fecha_estreno = datos['results'][0]['release_date']

# Mostramos los resultados por pantalla
print("Titulo de la pelicula: ",datos['results'][0]['title'])
print("Titulo original de la pelicula: ",datos['results'][0]['original_title'])
print("Popularidad: ",datos['results'][0]['popularity'])
print("Valoracion: ",datos['results'][0]['vote_average'])
print("Fecha de estreno: ",datos['results'][0]['release_date'])

# Mostramos por pantalla la descripcion de la pelicula
print("ARGUMENTO")
print("----------------------------------------------------------------------------------------")
print(datos['results'][0]['overview'])
print()


try:
    # Si el fichero existe hacemos las siguientes operaciones
    if open(fichero_txt):
        # primero lo abrimos para leer el contenido de lo que hay en el fichero
        manejador = open(fichero_txt, "r")
        lista = manejador.readlines()
        num_linea = 1
        # recorremos el fichero y si el titulo de la pelicula ya esta en el archivo no la añadimos
        for linea in lista:
            num_linea +=1
            if titulo in linea:
                print("La pelicula ya esta en el fichero y no se puede agregar")
                manejador.close()
                exit(4)
        # si la pelicula no esta en el fichero debemos añadirla
        manejador = open(fichero_txt, "a")
        manejador.write(f"{num_linea}: {titulo} | {titulo_original} | {popularidad} | {valoracion} | {fecha_estreno}\n")
        manejador.close()
        print("Pelicula añadida correctamente al fichero")
        exit(8)
        print()

except FileNotFoundError:
    # si el fichero no existe previamente, tenemos que crearlo y añadir la pelicula pasada por parámetro
    print(f"El fichero no existe, y se procede a crearlo")
    manejador = open(fichero_txt, "w")
    manejador.write(f"{titulo} | {titulo_original} | {popularidad} | {valoracion} | {fecha_estreno} \n")
    manejador.close()




