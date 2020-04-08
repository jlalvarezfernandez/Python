'''
primos.py

'''

numero = input("Dime un numero y te diré si es primo:")
'''
for divisor in range(2,numero):
  print(numero, "entre", divisor, "es", numero//divisor, "con resto", numero % divisor)
'''

restosNulos = 0

for divisor in range(1,(int(numero)+1)):
  if int(numero) % divisor ==0:
    restosNulos +=1
if restosNulos == 2:
  print("El numero", numero, " es primo")
else:
  print("El numero", numero, " no es primo")
