'''
PROPOSITO 1. Usando esta API de OpenWeather que nos da el pronóstico del tiempo para una ciudad que se le pide al usuario
             de los siguientes cinco días, mostrar:

                    Temperatura media
                    mínima y máxima (en grados Celsius) para cada día y global.

             Tened en cuenta que las respuestas de esta api referentes a los días y horas usan el tiempo en formato UNIX (UTC).
'''
import json
import os
import time
import requests  # importamos requests para manejar peticiones http


# pedimos la ciudad
ciudad = str(input("Introduce la ciudad para ver sus temperaturas: "))

# datos para hacer la peticion GET
url = 'https://api.openweathermap.org/data/2.5/forecast'
parametros = {'q': ciudad,'units': 'metric','mode':'json', 'APPID':'f13188ece6f3d740bc6070c6c42acef0', 'lang':'es'}

# petición GET
r = requests.get(url, params=parametros)
if r.status_code != 200:
    print("Error al hacer la petición", r.status_code)
    exit(1)

# resultados
print("Petición URL:", r.url, "\n")
print("Status Code:", r.status_code, "\n")

# datos es un diccionario

datos = r.json()
print("Información devuelta:", datos, "\n")


# calculos

dias = dict()  # diccionario con clave el dia y valor de medicinas del dia
totales = list()  # lista de mediciones diarias
for medicion in datos['list']:
    # fecha y temperatur medicion
    dia = medicion['dt_txt'][0:10]
    temperatura = float(medicion['main']['temp'])
    # si no tenemos datos de ese dia creamos una nueva entrada en el diccionario
    if not dias.get(dia):
        dias[dia]= list()
    # añadimos medicion
    dias[dia].append(temperatura)
    totales.append(temperatura)


# resultados

print()
for dia,temps in dias.items():
    print(f"dia {dia[8:]}-{dia[5:7]}-{dia[0:4]}:\t Temperatura media: {(sum(temps)/len(temps)):.2f}º,minima {min(temps)}º y maxima: {max(temps)}º")

print()
print(f"Totales:\tTemperatura media: {(sum(totales)/len(totales)):.2f}º, Temperatura maxima: {max(totales)}º, Temperatura minima {min(totales)}º")

