# Comparison operators
# They are logic operators and they return a boolean value

a = 10
b = 3

print(f"equal: {a == b}") # check if both variables are equal
print(f"different: {a != b}") # check if both variables are different
print(f"higher: {a > b}") # check if variable a is higher than variable b
print(f"lower: {a < b}") # check if variable a is lower than variable b
print(f"higher or equal: {a >= b}") # check if variable a is higher o equal than variable b
print(f"lower or equal: {a <= b}") # check if variable a is lower or equal than variable b

c = "Python"
d = 'python'

print(f"equal: {c == d}") # check if both variables are equal
print(f"different: {c != d}") # check if both variables are different

e = 33
f = '33'

print(f"equal: {e == f}") # check if both variables are equal
print(f"different: {e != f}") # check if both variables are different


# Float comparation
x=3.3
print(f'El valor actual de x es {x}')
y = 1.1 + 2.2

#Al desarrolar la ecuacion por la referencia en memoria y la operacion en python tiene cierta precision diferente 
  
print(f'El valor actual de y es {y}')

  
#dos formas de comparar los flotantes: por strings (mas brusco) y matematica.

  
#Con String
print('Metodo con strings')
y_str = format(y, ".2g") # ".2g" nos sirve para indicar cuantos digitos queremos que nos conserve en el string. En este caso, se quedaran DOS digitos.
  
print(f'El valor de y convertido en string es: y_str => {y_str}')
print(f'La comparacion entre "x" convertido a string y y_str es {y_str == str(x)}')

 
#Matematica 
print('Metodo Matematico')
tolerance = 0.00001
print(f'x - y es igual a {x-y}')
#hacer valor absoluto
print(f'El valor absoluto de x - y es {abs(x-y)}')
  
#Debido a que x-y es mucho menor que la tolerancia (por la precision), se puede asumir que ambos numeros son "iguales". Si se agregan mas ceros despues del decimal, se reduce la tolerancia y por tanto, al buscar mucha mas precision en ambos numeros y compararlos se arrojara un falso.
print(abs(x - y) < tolerance)

 
#Tambien se puede usar round(y,1) para solo incluir un digito despues del decimal 
y_round = round(y,1)
print(f'El valor redondeado de y es {y_round}')


y = 1.1 + 2.2

# Da formato al número como una cadena de texto con el símbolo del euro y dos decimales
y_str = '€{:,.2f}'.format(y)

print(y_str)