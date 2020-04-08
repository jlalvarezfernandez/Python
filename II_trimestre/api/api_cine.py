'''
PROPOSITO    2. Queremos obtener las 5 películas "trending topic" semanal o del día en función del género de la misma.
                Al usuario le preguntamos si quiere un género concreto o si los quiere todos.
                Usaremos la API de themoviedb.org
                Para los géneros de las películas: https://developers.themoviedb.org/3/genres/get-movie-list
                Para el "trending topic": https://developers.themoviedb.org/3/trending/get-trending

'''
import requests, os

if __name__ == '__main__':

    while True:
        # os.system("cls")
        print("Esta API nos muestra el trending actual de películas.")
        print("1) Todos los géneros")
        print("2) Por género ")
        print()
        option = int(input("Selecciona una opción:"))

        if option == 1:

            while True:
                os.system("cls")
                print("Elige el trending:")
                print("1) Diario")
                print("2) Semanal")
                general_option = int(input("Selecciona una opción:"))

                if general_option == 1:
                    url = "https://api.themoviedb.org/3/trending/movie/day"
                    args = {'api_key': '129807c4433110ade67bfb708f895d33', 'language': 'es-ES'}

                    response = requests.get(url, params=args)
                    print("Estado de la petición: ", response)
                    print("Petición url: ", response.url)

                    datos = response.json()

                    ranking = {"Peliculas": [], "Popularidad": []}
                    contador = 0
                    print("----- TRENDING DIARIO -----")
                    for t in datos['results']:
                        if contador < 5:
                            contador += 1
                            print(contador, "-", t['title'])
                            """
                            movie = t['title']
                            popularity = t['popularity']
                            ranking["Peliculas"].append(movie)
                            ranking["Popularidad"].append(popularity)
                            """

                    print("----------------------------")

                    break

                elif general_option == 2:
                    os.system("cls")

                    url = "https://api.themoviedb.org/3/trending/movie/week"
                    args = {'api_key': '129807c4433110ade67bfb708f895d33', 'language': 'es-ES'}

                    response = requests.get(url, params=args)
                    print("Estado de la petición: ", response)
                    print("Petición url: ", response.url)

                    datos = response.json()

                    # ranking = {"Peliculas": [], "Popularidad": []}
                    contador = 0
                    print("----- TRENDING DIARIO -----")
                    for t in datos['results']:
                        if contador < 5:
                            contador += 1
                            print(contador, "-", t['title'])
                            """
                            movie = t['title']
                            popularity = t['popularity']
                            ranking["Peliculas"].append(movie)
                            ranking["Popularidad"].append(popularity)
                            """

                    print("----------------------------")

                    break

                else:
                    os.system("cls")
                    print("No has introducido una opción correcta")
                    print("Vuelve a intentarlo")

        if option == 2:

            while True:
                os.system("cls")
                print("1) Ver géneros")
                print("2) Trending diario")
                print("3) Trending semanal")
                genre_option = int(input("Selecciona una opción:"))

                if genre_option == 1:
                    os.system("cls")

                    url = "https://api.themoviedb.org/3/genre/movie/list?"
                    args = {'api_key': '129807c4433110ade67bfb708f895d33', 'language': 'es-ES'}

                    response = requests.get(url, params=args)
                    print("Estado de la petición: ", response)

                    datos = response.json()

                    print("Todos los géneros")
                    for t in datos['genres']:
                        print(f" {t['name']} con id {t['id']}")

                    print("----------------------------")

                    break
                elif genre_option == 2:
                    os.system("cls")
                    url = "https://api.themoviedb.org/3/trending/movie/week"
                    args = {'api_key': '129807c4433110ade67bfb708f895d33', 'language': 'es-ES'}

                    response = requests.get(url, params=args)
                    print("Estado de la petición: ", response)
                    print("Petición url: ", response.url)

                    datos = response.json()

                    print("Trending diario")
                    genres = int(input("Selecciona un genero para saber el trending diario:"))

                    contador = 0
                    while contador < 5:
                        for t in datos['results']:
                            if genres == t['genre_ids']:
                                contador += 1
                                print(f" {contador} - {t['title']}")

                    break
                elif genre_option == 3:
                    os.system("cls")
                    print("Trending semanal")
                else:
                    os.system("cls")
                    print("No has introducido una opción correcta ostias")
                    print("Vuelve a intentarlo")

    else:
        print("No has introducido una opción correcta")
        print("Vuelve a intentarlo")