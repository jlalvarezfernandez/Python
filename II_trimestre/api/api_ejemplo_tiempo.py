"""
Calidad del aire en Córdoba.
Más info: http://www.juntadeandalucia.es/medioambiente/site/portalweb/menuitem.7e1cf46ddf59bb227a9ebe205510e1ca/

Usamos la API de openaq: https://docs.openaq.org/
"""
import requests
import json

# datos para hacer la petición GET
url = 'https://api.openaq.org/v1/latest'
parametros = {'city':'Cordoba', 'parameter':'no2'}

# peticion GET

r = requests.get(url, params=parametros)

# resultados
print("Petición URL:", r.url, "\n")
print("Status Code:", r.status_code, "\n")

datos = r.json()
print("Información devuelta:", datos, "\n")

print("Mediciones:")
for loc in datos['results']:
    print("-" + loc['location'], loc['measurements'])