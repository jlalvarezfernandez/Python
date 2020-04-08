'''
    proposito   2. Queremos obtener las 5 películas "trending topic" semanal o del día en función del género de la misma.
                   Al usuario le preguntamos si quiere un género concreto o si los quiere todos.
                   Usaremos la API de themoviedb.org
                   Para los géneros de las películas: https://developers.themoviedb.org/3/genres/get-movie-list
                   Para el "trending topic": https://developers.themoviedb.org/3/trending/get-trending
'''

# lo primero que tenemos que hacer es importar requests para manejar peticiones http
# importamos json

import requests
import json

# introducimos los datos para hacer la peticion GET

# url para hacer la peticion GET para obtener el trending topic diario de las peliculas
url = 'https://api.themoviedb.org/3/trending/movie/day?api_key=4e820182a07f0c85e3954f4735547ebe'

# url para hacer la peticion GET para obtener el trending topc semanal de las peliculas
url = 'https://api.themoviedb.org/3/trending/movie/week?api_key=4e820182a07f0c85e3954f4735547ebe'

# introducimos los parametros que vamos a usar

parametros = {'api_key': '4e820182a07f0c85e3954f4735547ebe', 'language': 'es-ES'}


# hacemos la petición GET
r = requests.get(url, params=parametros)

# condicional para mostrar error si la url esta mal puesta

if r.status_code != 200:
    print("Error al hacer la petición", r.status_code)
    exit(1)

# resultados
print("Petición URL:", r.url, "\n")
print("Status Code:", r.status_code, "\n")


# creamos un diccionario para alamcenar los datos json y los mostramos
diccionario = r.json()
print("Información devuelta:", diccionario, "\n")

# calculos para obtener la información del trending topic diario y semanal
contador = 0
for i in diccionario ['results']:
    print("Las peliculas mas populares son: ", i['title'])





