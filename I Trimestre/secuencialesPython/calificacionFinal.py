# Programa: Ejercicio10 calificacionFinal.py
#
# Proposito:  Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los siguientes porcentajes:
#             55% del promedio de sus tres calificaciones parciales.
#             30% de la calificación del examen final.
#             15% de la calificación de un trabajo final
# 
#
# @author: Álvarez Fernández José Luis
# Fecha : 10/10/2019
#
#
# Variables a usar
# parcial1 (númerica): almacenará la nota del primer parcial 
# parcial2 (númerica): almacenará la nota del segundo parcial 
# parcial3 (númerica): almacenará la nota del tercer parcial 
# examenFinal (númerica): almacenará la nota del examen final 
# trabajoFinal (númerica): almacenará la nota del trabajo final.
# notaFinalParciales (numérica): almacenara la nota media porcentuada de los tres parciales (parcial1 + parcial2 + parcial3)/ 3 * 0.55
# notaFinalExamen (numérica): alamcenará la nota porcentuada del examen final (examenFinal * 0.30)
# notaFinalExamen (numérica): almacenará la nota porcentuada del trabajo final (trabajoFinal * 0.15)
# notaFinalCurso (numérica): alamcenará la nota final del curso del alumno ( notaFinalParciales + notaFinalExamen + notaFinalTrabajo)
#
# Algoritmo:
#
# LEER parcial1, parcial2, parcial3, examenFinal, trabajoFinal 
# CALCULAR notaFinalParciales, notaFinalExamen, notaFinalExamen, notaFinalCurso
# ESCRIBIR notaFinalCurso


#Pedimos al usuario que introduzca la informacion por pantalla

#notas de los parciales
parcial1 = float(input("Introduce la nota del primer parcial: "))
parcial2 = float(input("Introduce la nota del segundo parcial: "))
parcial3 = float(input("Introduce la nota del tercer parcial: "))

#nota del examen final
examenFinal = float(input("Introduce la nota del examen final: "))

#nota del trabajo final
trabajoFinal = float(input("Introduce la nota del trabajo final: "))


#operaciones

notaFinalParciales = (parcial1 + parcial2 + parcial3)/ 3 * 0.55

notaFinalExamen = examenFinal * 0.30

notaFinalTrabajo = trabajoFinal * 0.15

notaFinalCurso = "{0:.2f}".format(notaFinalParciales + notaFinalExamen + notaFinalTrabajo)

#Mostramos los resultados por pantalla

print("La nota final del alumno en la asignatura de algoritmos será de: ",notaFinalCurso) 
