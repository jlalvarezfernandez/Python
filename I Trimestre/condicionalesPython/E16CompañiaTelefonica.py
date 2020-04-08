'''
Programa: Ejercicio 16 E16CompañiaTelefonica.py

Proposito:  La política de cobro de una compañía telefónica es: 
            cuando se realiza una llamada, el cobro es por el tiempo que ésta dura,
            de tal forma que los primeros cinco minutos cuestan 1 euro,
            los siguientes tres, 80 céntimos, 
            los siguientes dos minutos, 70 céntimos, 
            y a partir del décimo minuto, 50 céntimos. 
            Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día, 
            en turno de mañana, 15 %, y en turno de tarde, 10 %. 
            Realice un algoritmo para determinar cuánto debe pagar por cada concepto una persona 
            que realiza una llamada.


@author: Álvarez Fernández José Luis

Fecha : 17/10/2019
'''
'''
variables a usar:
tiempoLlamada (numérica): almacenará el tiempo de duracion en minutos de la llamada
domingo (str): almacenará si el dia elegido apra llamar es domingo
turno (str): almacenará si el turno en el que se produce la llamada es por la mañana o por la tarde
precio (númerica): almacenará el precio de la llamada segun los minutos de duración

Algoritmo:

LEER: tiempoLlamada, domingo, turno  
CALCULAR: precio de la llamada según minutos
            si son 5 o menos pagara 1 euro
            si son mas de 5 y y 8 min pagara 0.80 + los 5 euros anteriores
            si son entre 9 y 10 min pagara 0.70 + 1.60 + 5
            si son mas de 10 min pagara 0.50 + 8.80 
          si es domingo pagara ademas un recargo del 3% al total del precio
          si es de lunes a sabado en horario de mañana pagara 15% al total de la llamada
          si es de lunes a sabado en horario de tarde pagara 10% al total de la llamada
ESCRIBIR: precio
'''

# Pedimos al usuario que introduzca los datos por pantalla

tiempoLlamada = int(input("Introduce los minutos que durá tu llamada: "))


# Calculos

if tiempoLlamada < 5:
    precio = tiempoLlamada * 1
elif tiempoLlamada >5 or tiempoLlamada <=8:
    precio = tiempoLlamada - 5 * 0.80 + 5
elif tiempoLlamada > 8 or tiempoLlamada <= 10:
    precio = tiempoLlamada - 8 * 0.70 + 7.40
else:
    precio = tiempoLlamada - 10 * 0.50 + 8.80

domingo = input("¿Es domingo (S/N): ")
if domingo =="N" or domingo == 'n':
    turno = input("Como es un dia diferente a domingo, ingresa un turno de mañana o tarde (M/T)?: ")
if domingo =="S" or domingo =='s':
    precio += precio * 0.03
elif turno == "M" or turno =='m':
    precio += precio *0.15
elif turno == 'T' or turno == 't':
    precio += precio*0.10


# Mostramos los resultados por pantalla
 
print("El precio de la llamada es de: ", precio, "euros")

