# Programa: Ejercicio19 notaFinal.py
#
# Proposito:  Escribir un algoritmo para calcular la nota final de un estudiante, 
#             considerando que por cada respuesta correcta 5 puntos, por una incorrecta -1 y por respuestas en blanco 0. 
#             Imprime el resultado obtenido por el estudiante.
# 
#
# @author: Álvarez Fernández José Luis
# Fecha : 10/10/2019
#
#
# Variables a usar
# respCorrecta (númerica): almacenará el número de respuestas correctas 
# respIncorrecta (numérica): almacenará el número de respuestas incorrectas
# respBlanco (numérica): almacenará el número de respuestas en blanco
# totalPuntos (numérica): almacenará la cantidad de puntos obtenidos (respCorrecta * 5 + respIncorrectas * (-1) + respBlanco * 0)
# totalRespuestas (numérica) : almacenará el número total de respuestas
#notaFinal (numérica): almacenará la nota final del estudiante ((10 * totalPuntos)  / (totalRespuestas * 5 ))
#
# Algoritmo:
#
# LEER respCorrecta, respIncorrecta, respBlanco
# CALCULAR totalPuntos, totalRespuestas, notaFinal
# ESCRIBIR notaFinal


# Pedimos al usuario que introduzca los datos por pantalla

respCorrecta = int(input("Introduce el número de respuestas correctas: "))
respIncorrectas = int(input("Introduce el número de respuestas incorrectas: "))
respBlanco = int(input("Introduce el número de respuestas en blanco: "))

# Calculos

totalPuntos =  (respCorrecta * 5 + respIncorrectas * (-1) + respBlanco * 0)
totalRespuestas = (respCorrecta + respIncorrectas + respBlanco)
notaFinal = "{0:.2f}".format(((10 * totalPuntos)  / (totalRespuestas * 5 )))

# Mostramos los resultados por pantalla

print ("tu nota final es: ",notaFinal)

