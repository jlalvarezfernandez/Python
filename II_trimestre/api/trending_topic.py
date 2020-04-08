"""
 Queremos obtener las 5 películas "trending topic" semanal o del día en función del género de la misma.

Al usuario le preguntamos si quiere un género concreto o si los quiere todos.

Usaremos la API de themoviedb.org

Para los géneros de las películas: https://developers.themoviedb.org/3/genres/get-movie-list

Para el "trending topic": https://developers.themoviedb.org/3/trending/get-trending
"""

import requests
import json
"""
Función que realiza la petición en la API, se la pasa como parámetro el género (id del género) y el trending
(constará de diario o semanal)
"""



def peticion(trending):
    contador_peli = 0
    pagina = 1
    genero = 0

    # Realizamos petición
    url = "https://api.themoviedb.org/3/trending/movie/"
    args = {'api_key': '4e820182a07f0c85e3954f4735547ebe', 'language': 'es-ES', 'page': pagina}

    if trending == "diario":
        url += str("day")
    if trending == "semanal":
        url += str("week")
    response = requests.get(url, params=args)
    if 200 != response.status_code:
        print(f"Ha habido un fallo en la petición {response.status_code}")
        exit(1)

    datos = response.json()

    #if not genero or genero


    for p in datos ['results']:
        if contador_peli < 5:
            contador_peli += 1
            print(" Titulo: ", p['title'])


if __name__ == '__main__':
    trending = input("Introduce trending que deseas ver: (diario/semanal): ")
    #genero = int(input("Introduce id del género: "))

    peticion(trending)




