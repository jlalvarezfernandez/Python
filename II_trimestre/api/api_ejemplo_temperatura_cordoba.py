"""
EJEMPLOS DE EJERCICIOS APIs EN PYTHON

TEMPERATURA EN CÓRDOBA


Usamos la API de openweather: https://openweathermap.org/api
Es necesario registrarse
'APPID':'f13188ece6f3d740bc6070c6c42acef0'
"""

# importamos las clases necesarias

import requests
import json
import time


# datos para hacer lo petición GET

api_key = 'f13188ece6f3d740bc6070c6c42acef0'
url = "https://api.openweathermap.org/data/2.5/weather"
parametros = {'q':'Cordoba,es', 'APPID':api_key, 'mode':'json', 'units': 'metric', 'lang':'es'}

# hacemos la petición GET

response = requests.get(url, params=parametros)

# Mostramos los resultados de la petición
print("Página web utilizada:", response.url)
print("Estado de hacer la petición, código:",response.status_code)

if response.status_code == 200:
    print("Petición correcta")
else:
    print("Error al hacer la petición")

#sacamos un diccionario con los datos de la peticion. nos devuelve la información en ese formato
datos = response.json()

# imprimimos la información devuelta y añadimos soporte multilingue

parametros['lang'] = 'es'
response = requests.get(url,params=parametros)
print("Información devuelta:",response.json())

# ahora accedemos a los datos

print("Resultados de las mediciones")
print("Localización: ",datos['name'],datos['sys']['country'], "con coordenadas","[",{datos['coord']['lat']},{datos['coord']['lon']},"]")
print("Fecha",time.ctime(datos['dt']))

# mostramos los resultados

for temperaturas in datos['weather']:
    print("Tiempo:", temperaturas['description'])

print()
# mostramos las mediciones
print("Mediciones")
print("Temperatura:", datos["main"]["temp"], "ºC")
print("Presión: ", datos['main']['pressure'],"hPa")
print("Humedad: ",datos['main']['humidity'], "%")
print("Velocidad del Viento: ",datos['wind']['speed'], "km/hora")














