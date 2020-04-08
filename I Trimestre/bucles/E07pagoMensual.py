'''
Programa: Ejercicio 7 E07pagoMensual.py

Proposito: Una persona adquirió un producto para pagar en 20 meses. 
             El primer mes pagó 10 €, 
             el segundo 20 €, 
             el tercero 40 € y así sucesivamente. 
             Realizar un programa para determinar cuánto debe pagar mensualmente 
             y el total de lo que pagará después de los 20 meses.

@author: Álvarez Fernández José Luis

Fecha : 26/10/2019

'''
'''
variables:
pagoMensual (numérica): se incia en 10, porque el priemr pago será de 10 euros
totalPago (numérica): se inicia en  porque todavia no sabemos lo que va  apagar
mes (numérica): se inciia en  porque todavia no se han incrementado los meses

Algoritmo

CALCULAR: bucle for-in para que recorra los 20 meses en los que se fracciona el pago
          totalPago se incrementa en cada pagoMensual, asi 20 veces y obtenemos el total que va a pagar
          pagoMensual se incremeta multiplicado por 2 porque cada mes paga el doble

ESCRIBIR: totalPago


'''

# Calculos
pagoMensual = 10
totalPago = 0
mes = 0

for mes in range(1,21):
    print("en el mes ",mes," paga: ", pagoMensual, "euros")
    totalPago +=  pagoMensual
    pagoMensual *= 2
    
# Mostramos los resultados por pantalla
   
print("total: ", totalPago, "euros")