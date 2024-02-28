# Clasic list
numbers = []
for i in range(1, 11):
  numbers.append(i * 2)
print(numbers, '\n')
    
# List comprehensions basic

numbers_2 = [i*2 for i in range(1,11)]

print(numbers_2,'\n')

# List comprehensions 2 variables whit conditionals

numbers_3 = [[i,j] for i in range(1,11) if i % 2 == 0 for j in range(1,11) if j % 2 != 0]

print(numbers_3, '\n')

# Operadoes ternarios en list comprehension

lista = [5, 7, 11, 12, 15, 20, 24]
lista_nueva = [ elemento * 2 if elemento < 15 else elemento / 2 for elemento in lista ]

print(lista_nueva, '\n')

# nested if

numbers = [1,2,3,4,5,6,7,8,9,10]
iterate_numbers = [i for i in numbers if i > 4 if i % 2 == 0]

print(iterate_numbers)