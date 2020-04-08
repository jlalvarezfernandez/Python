'''
programa que calcule la suma, tresta, division, multiplicacion de dos numeros introducidos por teclado
usaremos funciones
usaremos excepciones para el manejo de errores

'''

# funciones

def suma (num1,num2):
    return num1+num2

def resta (num1,num2):
    return num1-num2

def division (num1,num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        print("Error no se puede dividir entre 0")
        return "operacion cancelada"

def multiplicacion (num1,num2):
    return num1*num2


# pedimos los datos
while True:
    try:

        numero1= int(input("Introduce el primer número: "))

        numero2 = int(input("Introduce el segundo número: "))
        break

    except:
        print("Error, debes introducir un nuemro entero")

operacion = str(input("Introduce la operacion a realizar (suma, resta, division, multiplicacion): "))


# calculos

if operacion == "suma":
    print(suma(numero1,numero2))
elif operacion == "resta":
    print(resta(numero1,numero2))
elif operacion == "division":
    print(division(numero1,numero2))
elif operacion == "division":
    print(multiplicacion(numero1,numero2))
else:
    print("Error!!!")

print("Fin operaciones, continua el programa")

