"""
PROPOSITO: 2. Queremos obtener las 5 películas "trending topic" semanal o del día en función del género de la misma.
              Al usuario le preguntamos si quiere un género concreto o si los quiere todos.

                  Usaremos la API de themoviedb.org

                  Para los géneros de las películas: https://developers.themoviedb.org/3/genres/get-movie-list

                  Para el "trending topic": https://developers.themoviedb.org/3/trending/get-trending

              Para esta versión utilizaré metodos para modularizar y simplificar el código haciendolo mas legible
"""
import  requests
import os
"""
Métodos para el ejercicio
"""
def peticion(opcion, genero):
    num_pelis = 0
    pagina = 1
    url_todos = URL_BASE + TRENDING_TOPIC

    if opcion == 1:
        url_todos += DIARIO
    elif opcion == 2:
        url_todos += SEMANAL
    elif opcion == 3:
        url_todos += SEMANAL
    else:
        print("Petición incorrecta")

    print("Resultados:")
    while True:
        parametros = {'api_key': API_KEY, 'language': 'es-ES', 'page': str(pagina)}
        # Hacemos la petición GET
        response = requests.get(url_todos, params=parametros)
        if response.status_code != 200:
            print("Petición incorrecta")
            exit(1)
        datos = response.json()
        # bucle for que recorre los resultados y nos muestra el nombre de las 5 primers películas
        for peliculas in datos['results']:
            if (genero == 0) or (genero in peliculas['genre_ids']):
                if num_pelis < 5:
                    num_pelis += 1
                    print(num_pelis, ") Título:", peliculas['title'])
        pagina += 1

def id_generos():
    url = URL_BASE + GENEROS
    parametros = {'api_key': API_KEY, 'language': 'es-ES'}
    # Hacemos la petición GET
    response = requests.get(url=url, params=parametros)
    # mostramos los datos de hacer la petición
    if response.status_code != 200:
        print("Petición incorrecta")
        exit(1)
    datos = response.json()
    print("Generos disponibles")
    for generos in datos['genres']:
        print("Código:\t", generos['id'], "\tgénero:\t", generos['name'])
    print()

if __name__ == '__main__':
    """
    Declaramos unas constantes que usaremos a lo largo de todo el ejercicio
    """
    URL_BASE = "https://api.themoviedb.org/3"
    # endpoint que se anexará a la url base para filtrar cuando queramos mostrar el trending topic de las películas
    TRENDING_TOPIC = "/trending/movie"
    # endpoint que se anexará a la url base + trending topic para filtar peliculas por dia
    DIARIO = "/day"
    # endpoint que se anexará a la url base + trending topic para filtar peliculas por semana
    SEMANAL = "/week"
    # endpoint para filtar por generos
    GENEROS = "/genre/movie/list"
    # cosntante para mostrar simepre 5 peliculas segun las opciones elegidas
    TOTAL_PELICULAS = 5
    # Almacenará la clave de la Api, asi no tendre que escribirla siempre
    API_KEY = os.environ['movie_api']
    genero = 0

    print("--------API PARA OBTENER 5 PELICULAS TRENDING TOPIC--------")
    # datos para mostrar la url general de la API
    print()
    print("PÁGINA WEB USADA: ", URL_BASE)
    print("------------------------------------------------------------")
    while True:
        print("Elige una de las siguientes opciones: ")
        print()
        print("A.- Películas por todos los géneros")
        print("B.- Películas por géneros")
        print()
        opcion = input("Introduce tu opción (A o B): ")
        print()
        if opcion.upper() == "A":
            while True:
                print("Has elegido ver el trending topic de películas por todos los géneros")
                print("¿Que te apetece ver?:")
                print("--------------------")
                print("1.- Trending diario")
                print("2.- Trending semanal")
                print()
                opcion_todos_generos = int(input("Introduce tu opción (1/2): "))
                if opcion_todos_generos == 1:
                    peticion(opcion_todos_generos,genero)
                    break

                elif opcion_todos_generos == 2:
                    peticion(opcion_todos_generos,genero)
                    break
                else:
                    print("Opción introducida incorrecta")
            break

        if opcion.upper() == "B":
            opcion_generos = 0
            codigo_genero = 0
            while True:
                try:
                    print("Has elegido ver el trending topic de películas por género")
                    print("¿Que te apetece ver?:")
                    print()
                    print("1.- Todos los géneros")
                    print("2.- Trending diario")
                    print("3.- Trending semanal")
                    opcion_generos = int(input("Introduce tu opción (1/2/3): "))
                    if opcion_generos == 2 or opcion_generos == 3:
                        codigo_genero = int(input("Introduce el código del género del que quieres ver el trending topic semanal: "))
                except ValueError:
                    print("Código erroneo, introduce un código correcto")
                print()

                if opcion_generos == 1:
                    id_generos()
                elif opcion_generos == 2:
                    peticion(opcion_generos, codigo_genero)
                    break
                elif opcion_generos == 3:
                    peticion(opcion_generos, codigo_genero)
                    break
                else:
                    print("Opción introducida incorrecta")
            break




