"""
PROPOSITO: 1. Usando esta API de OpenWeather que nos da el pronóstico del tiempo para una ciudad
              que se le pide al usuario de los siguientes cinco días, mostrar:

                    Temperatura media, mínima y máxima (en grados Celsius) para cada día y global.

              Tened en cuenta que las respuestas de esta api referentes  a los días y horas usan el tiempo
              en formato UNIX (UTC).
"""
# importamos las clases que vamos a utilizar

import requests
import os # para poder crear una variable de entorno en python

# pedimos al usuario que introduzca los datos por teclado

ciudad = input("Ciudad de la que quiere conocer el pronóstico del tiempo en los próximos 5 días: ")

# datos para hacer la petición GET

url ="https://api.openweathermap.org/data/2.5/forecast"
api_key = 'f13188ece6f3d740bc6070c6c42acef0'
parametros ={'q':ciudad, 'APPID':api_key,'units':'metric','lang':'es','mode':'json'}

# hacemos la petición GET
response = requests.get(url,params=parametros)

# Mostramos la información de la peticion

print("Página utilizada:", url)
print("Código de estado de la petición GET", response.status_code)

if response.status_code == 200:
    print("Petición correcta")
else:
    print("Error al hacer la petición")

#sacamos un diccionario con los datos de la peticion. Nos devuelve la información en ese formato
datos = response.json()

# usamos un diccionario llamado dias que tendra otro diccionario vacio que tendra una clave por cada dia y devolverá una
# lista con las medidas de las temperaturas.

dias = dict()

# despues usamos una lista llamada totales donde se guardan todas las temperaturaspara calcular el minimo, maximo y media
# hacemos como en el anterior y que despues convertiremos en un diccionario

totales = {"temp": [], "temp_min": [], "temp_max": []}


print("Mostramos los resultados")
print("------------------------")

# bucle for que se desplaza por list, en cada iteración recorre las
#temperaturas medias, minimas y maximas

for medicion in datos['list']:
    # sacamos los datos de las mediciones de cada dia
    dia = medicion["dt_txt"][:10] # la fecha del dia son los 10 priemros caracteres
    temperatura = medicion['main']['temp']
    temp_minima = medicion['main']['temp_min']
    temp_maxima = medicion['main']['temp_max']

    # si no tenemos datos de ese día creamos una nueva entrada en el diccionario
    if not dias.get(dia):
        dias[dia] = {"temp": [], "temp_min": [], "temp_max": []}

    # añadimos a la lista las mediciones
    dias[dia]["temp"].append(temperatura)
    dias[dia]["temp_min"].append(temp_minima)
    dias[dia]["temp_max"].append(temp_maxima)
    totales["temp"].append(temperatura)
    totales["temp_min"].append(temp_minima)
    totales["temp_max"].append(temp_maxima)

# resultados
print()
# ponemos el resultado de los dias, recoriendo el diccionario de los dias y usamos dos claves dia y temps
for dia, temps in dias.items():
    # diario
    temp_media = sum(temps['temp']) / len(temps['temp'])
    temp_minima = min(temps['temp_min'])
    temp_maxima = max(temps['temp_max'])
    print(f"Día {dia[8:]}-{dia[5:7]}-{dia[0:4]}:\t"
          f"Temperatura media: {temp_media:.2f}º, "
          f"mínima: {temp_minima}º y máxima: {temp_maxima}º. "
          f"Mediciones: {len(temps['temp'])}")
print()

# global
temp_med = sum(totales['temp']) / len(totales['temp'])
temp_min = min(totales['temp_min'])
temp_max = max(totales['temp_max'])
print(f"TOTALES:\t\tTemperatura media: {temp_med:.2f}º, "
      f"mínima: {temp_min}º y máxima: {temp_max}º")





