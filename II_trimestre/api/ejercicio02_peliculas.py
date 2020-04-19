"""
PROPOSITO: 2. Queremos obtener las 5 películas "trending topic" semanal o del día en función del género de la misma.
              Al usuario le preguntamos si quiere un género concreto o si los quiere todos.

                  Usaremos la API de themoviedb.org

                  Para los géneros de las películas: https://developers.themoviedb.org/3/genres/get-movie-list

                  Para el "trending topic": https://developers.themoviedb.org/3/trending/get-trending
"""

# importamos requets
import requests

print("--------API PARA OBTENER 5 PELICULAS TRENDING TOPIC--------")
# datos para mostrar la url general de la API
url_base = "https://api.themoviedb.org/3"
print()
print("PÁGINA WEB USADA: ", url_base)
print("------------------------------------------------------------")
while True:
    print("Elige una de las siguientes opciones: ")
    print()
    print("1.- Películas por todos los géneros")
    print("2.- Películas por géneros")
    print()

    opcion = int(input("Introduce tu opción (1/2): "))
    print()

    if opcion == 1:
        while True:
            print("Has elegido ver el trending topic de películas por todos los géneros")
            print("¿Que te apetece ver?:")
            print("--------------------")
            print("1.- Trending diario")
            print("2.- Trending semanal")
            print()
            opcion_todos_generos = int(input("Introduce tu opción (1/2): "))

            if opcion_todos_generos == 1:

                # datos para hacer la petición

                api_key = '242f6331a4ccccac0111863d092cbdbf'
                url_diaria_todos = "https://api.themoviedb.org/3/trending/movie/day"
                parametros = {'api_key': api_key, 'language': 'es'}

                # Hacemos la petición GET

                response = requests.get(url=url_diaria_todos,params=parametros)

                # mostramos los datos de hacer la petición

                print("Estado de hacer la petición: código ==>", response.status_code)
                print("url utilizada: ", url_diaria_todos)

                # Comprobamos estado de la petición

                if response.status_code == 200:
                    print("Petición correcta")
                else:
                    print("Petición incorrecta")
                    exit(1)

                # sacamos un diccionario con los datos de la peticion. Nos devuelve la información en ese formato
                datos = response.json()

                # bucle for que recorre los resultados y nos muestra el nombre de las 5 primers películas

                contador = 0
                print("Resultados:")
                for peliculas in datos['results']:
                    if contador < 5:
                        contador += 1
                        print(contador, ") Título:", peliculas['title'])
                break


            elif opcion_todos_generos == 2:

                # datos para hacer la petición
                api_key = '242f6331a4ccccac0111863d092cbdbf'
                url_diaria_todos = "https://api.themoviedb.org/3/trending/movie/week"
                parametros = {'api_key': api_key, 'language': 'es'}

                # Hacemos la petición GET

                response = requests.get(url=url_diaria_todos, params=parametros)

                # mostramos los datos de hacer la petición

                print("Estado de hacer la petición: código ==>", response.status_code)
                print("url utilizada: ", url_diaria_todos)

                # Comprobamos estado de la petición

                if response.status_code == 200:
                    print("Petición correcta")
                else:
                    print("Petición incorrecta")
                    exit(1)

                # sacamos un diccionario con los datos de la peticion. Nos devuelve la información en ese formato
                datos = response.json()

                # bucle for que recorre los resultados y nos muestra el nombre de las 5 primers películas

                contador = 0
                print("Resultados:")
                for peliculas in datos['results']:
                    if contador < 5:
                        contador += 1
                        print(contador, ") Título:", peliculas['title'])
                break

            else:
                print("Opción introducida incorrecta")

        break
    if opcion == 2:
        while True:
            print("Has elegido ver el trending topic de películas por género")
            print("¿Que te apetece ver?:")
            print()
            print("1.- Todos los géneros")
            print("2.- Trending diario")
            print("3.- Trending semanal")
            print()
            opcion_generos = int(input("Introduce tu opción (1/2/3): "))

            if opcion_generos == 1:
                # datos para hacer la petición
                api_key = '242f6331a4ccccac0111863d092cbdbf'
                url_diaria_todos = "https://api.themoviedb.org/3/genre/movie/list"
                parametros = {'api_key': api_key, 'language': 'es'}

                # Hacemos la petición GET

                response = requests.get(url=url_diaria_todos, params=parametros)
                # mostramos los datos de hacer la petición

                print("Estado de hacer la petición: código ==>", response.status_code)
                print("url utilizada: ", url_diaria_todos)

                # Comprobamos estado de la petición

                if response.status_code == 200:
                    print("Petición correcta")
                else:
                    print("Petición incorrecta")
                    exit(1)

                # sacamos un diccionario con los datos de la peticion. Nos devuelve la información en ese formato
                datos = response.json()

                print("Generos disponibles")
                for generos in datos['genres']:
                    print("Código:\t",generos['id'],"\tgénero:\t",generos['name'])
                print()


            elif opcion_generos == 2:

                # datos para hacer la petición
                pagina = 1
                api_key = '242f6331a4ccccac0111863d092cbdbf'
                url_diaria_todos = "https://api.themoviedb.org/3/trending/movie/day"
                parametros = {'api_key': api_key, 'language': 'es', 'pages': str(pagina)}

                # Hacemos la petición GET

                response = requests.get(url=url_diaria_todos, params=parametros)

                # mostramos los datos de hacer la petición

                print("Estado de hacer la petición: código ==>", response.status_code)
                print("url utilizada: ", url_diaria_todos)

                # Comprobamos estado de la petición

                if response.status_code == 200:
                    print("Petición correcta")
                else:
                    print("Petición incorrecta")
                    exit(1)

                # sacamos un diccionario con los datos de la peticion. Nos devuelve la información en ese formato
                datos = response.json()
                codigo_genero= int(input("Introduce el código del género del que quieres ver el trending topic diario: "))

                # bucle for para mostrar las 5 primeras películas por trending topic diarias de un determinado genero
                print("Resultados:")
                contador = 0
                while True:
                    parametros = {'api_key': api_key, 'language': 'es-ES', 'page': str(pagina)}
                    # Hacemos la petición GET
                    response = requests.get(url_diaria_todos, params=parametros)
                    if response.status_code != 200:
                        print("Petición incorrecta")
                        exit(1)
                    datos = response.json()
                    # bucle for que recorre los resultados y nos muestra el nombre de las 5 primers películas

                    for peliculas in datos['results']:
                        if codigo_genero in peliculas['genre_ids']:
                            if contador < 5:
                                contador += 1
                                print(contador, ") Título:", peliculas['title'])
                    pagina += 1

            elif opcion_generos == 3:
                # datos para hacer la petición
                pagina = 1
                api_key = '242f6331a4ccccac0111863d092cbdbf'
                url_diaria_todos = "https://api.themoviedb.org/3/trending/movie/week"
                parametros = {'api_key': api_key, 'language': 'es', 'page': str(pagina)}

                # Hacemos la petición GET

                response = requests.get(url=url_diaria_todos, params=parametros)

                # mostramos los datos de hacer la petición

                print("Estado de hacer la petición: código ==>", response.status_code)
                print("url utilizada: ", url_diaria_todos)

                # Comprobamos estado de la petición

                if response.status_code == 200:
                    print("Petición correcta")
                else:
                    print("Petición incorrecta")
                    exit(1)

                # sacamos un diccionario con los datos de la peticion. Nos devuelve la información en ese formato
                datos = response.json()
                codigo_genero = int(
                    input("Introduce el código del género del que quieres ver el trending topic semanal: "))

                # bucle for para mostrar las 5 primeras películas por trending topic diarias de un determinado genero
                contador = 0
                print("Resultados")
                while True:
                    parametros = {'api_key': api_key, 'language': 'es', 'page': str(pagina)}
                    # Hacemos la petición GET
                    response = requests.get(url_diaria_todos, params=parametros)
                    if response.status_code != 200:
                        print("Petición incorrecta")
                        exit(1)
                    datos = response.json()
                    # bucle for que recorre los resultados y nos muestra el nombre de las 5 primers películas

                    for peliculas in datos['results']:
                        if codigo_genero in peliculas['genre_ids']:
                            if contador < 5:
                                contador += 1
                                print(contador, ") Título:", peliculas['title'])
                    pagina += 1

            else:
                print("Opción introducida incorrecta")
                print()
        break

    else:
        print("Opción introducida incorrecta")
        print()








