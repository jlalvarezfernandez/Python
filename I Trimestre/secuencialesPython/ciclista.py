
# Programa: Ejercicio17 ciclista.py
#
#
# Proposito:  Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo de viaje hasta llegar a otra ciudad B es de T segundos.
#             Escribir un algoritmo que determine la hora de llegada a la ciudad B.
# 
#
# @author: Álvarez Fernández José Luis
# Fecha : 10/10/2019
#
#
# Variables a usar
#
# hora (numérica): almacenará la hora de salida
# minutos (numérica): almacenará los minutos de salida 
# segundos (numérica): almacenará los segundos de salida
# segundosViaje (numérica): almacenará los segundos que dura el viaje
# tiempoSalida (numérica) : almacenará el tiempo de salida en segundos (tiempoSalida = ((hora * 3600) + (minutos * 60) + (segundos)))
# tiempoTotal (numérica): almacenará el tiempo total del viaje (tiempoTotal = (tiempoSalida + segundosViaje))
# segundosViaje (numérica): almacenará la hora de llegada ((tiempoTotal / 3600))
# minutosLlegada (numérica): almacenará los minutos a los que llega ((tiempoTotal % 3600) / 60)
# segundosLLegada (numérica): almacenará los segundos a los que llega ( (tiempoTotal % 3600) % 60



# Algoritmo:
#
# LEER hora, minutos, segundos, segundosViaje
# CALCULAR  tiempoSalida, tiempoTotal, horaLlegada, minutosLlegada, segundosLlegada
# ESCRIBIR  horaLlegada, minutosLlegada, segundosLlegada


# Pedimos al usuario que introduzca los datos por pantalla

hora = int(input("Introduce la hora de salida del ciclista: "))
minutos = int(input("Introduce los minutos de salida del ciclista: "))
segundos = int(input("Introduce los segundos de salida del ciclista: "))
segundosViaje = int(input("Introduce los segundos que dura el viaje: "))

# Calculos

tiempoSalida = ((hora * 3600) + (minutos * 60) + (segundos))  # asi calculo el tiempo de salida en segundos

tiempoTotal = (tiempoSalida + segundosViaje) # el tiempo total del viaje se calcula sumando el tiempo de salida en segundos mas lo que dura el viaje en segundos

horaLlegada = (int)((tiempoTotal / 3600)) # para calcular la hora a la que llega

minutosLlegada =(int)((tiempoTotal % 3600) / 60) # para calcular a los min en que llega

segundosLlegada = (tiempoTotal % 3600) % 60 # para calcular a los segundos en que llega

# Mostramos los resultados por pantalla

print("La hora de llegada sera: ", horaLlegada, " horas " , minutosLlegada , " minutos " , segundosLlegada , " segundos")
	    
