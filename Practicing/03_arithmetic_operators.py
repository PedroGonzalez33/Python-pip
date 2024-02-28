# arithmetic operators

# adition
print(10 + 10)

# subtraction
print(10 - 5)

# multiplication
print(2 * 4)

# division
print(10 / 2)

# modulus or residue
print(10 % 3) # residue is 1
print(10 % 2) # residue is 0

# floor division
print(10 // 3)# with this operator only the integer of the division is captured. The result would be 3.

# exponentiation
print(2 ** 3) # 2^3 = 8
print(2 ** 3 + 3 - 7 / 1 // 4)
# print(x + 3 - y//z)
# x = 2 ** 3 = 8
# y = 7 / 1 = 7
# z = 4
# y // z = 7 // 4 = 1
# print(8 + 3 - 1)
# result = 10

# concatenate string
print("Holis " * 3) # Holis Holis Holis

'''
JERARQUIZACION:
LA PRIORIDAD ES DE IZQUIERDA A DERECHA
P - PARENTESIS
E - EXPONENTES
M - MULTIPLICACION
D - DIVISION
A - ADICION
S - SUSTRACCION
'''

# Exercice: pedir una cantidad de dinero a retirar en un cajero y imprimir la cantidad de billetes de cada denominación.
# Ejemplo: solicito 385 dolares, es decir, que son 3 billetes de 100, 1 de 50, 1 de 20, 1 de 10 y 1 de 5 dolares. 

while True:
  value = input("How many cash do you whant to retire: ")
  try:
    value = float(value)
    value = int(value)
    break
  except:
    print("Please introduce a numeric value")  

# Initialize variables
reste_100 = 0
reste_50 = 0
reste_20 = 0
reste_10 = 0
reste_5 = 0
reste_1 = 0
cash_100 = 0
cash_50 = 0
cash_20 = 0
cash_10 = 0
cash_5 = 0
cash_1 = 0

if value >= 100:
  reste_100 = (value // 100) * 100
  reste_100 = value - reste_100
  cash_100 = value // 100

  reste_50 = (reste_100 // 50) * 50
  reste_50 = reste_100 - reste_50
  cash_50 = reste_100 // 50

  reste_20 = (reste_50 // 20) * 20
  reste_20 = reste_50 - reste_20
  cash_20 = reste_50 // 20
  
  reste_10 = (reste_20 // 10) * 10
  reste_10 = reste_20 - reste_10
  cash_10 = reste_20 // 10

  reste_5 = (reste_10 // 5) * 5
  reste_5 = reste_10 - reste_5
  cash_5 = reste_10 // 5

  reste_1 = (reste_5 // 1) * 1
  reste_1 = reste_5 - reste_1
  cash_1 = reste_5 // 1

elif 50 <= value < 100:
  reste_50 = (value // 50) * 50
  reste_50 = value - reste_50
  cash_50 = value // 50

  reste_20 = (reste_50 // 20) * 20
  reste_20 = reste_50 - reste_20
  cash_20 = reste_50 // 20
  
  reste_10 = (reste_20 // 10) * 10
  reste_10 = reste_20 - reste_10
  cash_10 = reste_20 // 10

  reste_5 = (reste_10 // 5) * 5
  reste_5 = reste_10 - reste_5
  cash_5 = reste_10 // 5

  reste_1 = (reste_5 // 1) * 1
  reste_1 = reste_5 - reste_1
  cash_1 = reste_5 // 1

elif 20 <= value < 50:
  reste_20 = (value // 20) * 20
  reste_20 = value - reste_20
  cash_20 = value // 20
  
  reste_10 = (reste_20 // 10) * 10
  reste_10 = reste_20 - reste_10
  cash_10 = reste_20 // 10

  reste_5 = (reste_10 // 5) * 5
  reste_5 = reste_10 - reste_5
  cash_5 = reste_10 // 5

  reste_1 = (reste_5 // 1) * 1
  reste_1 = reste_5 - reste_1
  cash_1 = reste_5 // 1

elif 10 <= value < 20:
  reste_10 = (value // 10) * 10
  reste_10 = value - reste_10
  cash_10 = value // 10

  reste_5 = (reste_10 // 5) * 5
  reste_5 = reste_10 - reste_5
  cash_5 = reste_10 // 5

  reste_1 = (reste_5 // 1) * 1
  reste_1 = reste_5 - reste_1
  cash_1 = reste_5 // 1

elif 5 <= value < 10:
  reste_5 = (value // 5) * 5
  reste_5 = value - reste_5
  cash_5 = value // 5

  reste_1 = (reste_5 // 1) * 1
  reste_1 = reste_5 - reste_1
  cash_1 = reste_5 // 1

elif 1 <= value < 5:
  reste_1 = (value // 1) * 1
  reste_1 = value - reste_1
  cash_1 = value // 1

print(f'Your amount in cash is:\n{cash_100} -> 100$, \n{cash_50} -> 50$, \n{cash_20} -> 20$, \n{cash_10} -> 10$, \n{cash_5} -> 5$, \n{cash_1} -> 1$. \nThanks for your retire :D') 