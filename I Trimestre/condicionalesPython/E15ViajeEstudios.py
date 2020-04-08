'''
Programa: Ejercicio 15 E15ViajeEstudios.py

Proposito: El director de una escuela está organizando un viaje de estudios, 
           y requiere determinar cuánto debe cobrar a cada alumno 
           y cuánto debe pagar a la compañía de viajes por el servicio. 
           La forma de cobrar es la siguiente: 
                si son 100 alumnos o más, el costo por cada alumno es de 65 euros; 
                de 50 a 99 alumnos, el costo es de 70 euros, 
                de 30 a 49, de 95 euros, 
                y si son menos de 30, el costo de la renta del autobús es de 4000 euros, sin importar el número de alumnos. 
           Realice un algoritmo que permita determinar el pago a la compañía de autobuses
           y lo que debe pagar cada alumno por el viaje.


@author: Álvarez Fernández José Luis

Fecha : 17/10/2019
'''
'''
variables a usar:
totalAlumnos (numérica): almacenará el número de alumnos que van al viaje
precioViaje (numérica): almacenará el precio a pagar a la compañia 
precioAlumno (numérica): almacenará el precio que pagará cada alumno por ir al viaje
ladoC (numérica): almacenará el valor de un lado del triangulo


Algoritmo:

LEER: totalAlumnos  
CALCULAR: precioViaje (totalAlumnos * correspondiente precio de la tabla)
          precioAlumno ( totalAlumnos / 4000, cuando son menos de 30 alumnos), el resto según tabla
ESCRIBIR: precioViaje, precioAlumno
'''

# Pedimos al usuario que introduzca los datos por pantalla

totalAlumnos = int(input("Introduce el número de alumnos que van al viaje: "))

# Calculos

if totalAlumnos >= 100:
     precioViaje = totalAlumnos * 65
     precioAlumno = 65
elif totalAlumnos >= 50 and totalAlumnos <= 99:
     precioViaje = totalAlumnos * 70
     precioAlumno = 70
elif totalAlumnos >= 30 and totalAlumnos <= 49:
     precioViaje = totalAlumnos * 95
     precioAlumno = 95
else:
     precioViaje = 4000
     precioAlumno = 4000/totalAlumnos

# Mostramos los datos por pantalla

print("El precio a pagar por el viaje según el número de alumnos será de: ", precioViaje, "euros y cada alumno pagará", precioAlumno, "euros")

