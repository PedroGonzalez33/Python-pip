# lambda arguments : expression

increment_v2 = lambda x : x + 1

result = increment_v2(20)
print(result,'\n') # 21

# Comparacion con lambda
print((lambda x: x % 2 == 0)(4))

# La función lambda puede tomar cualquier cantidad de argumentos, pero solo puede tener una expresión.

datos_completos = lambda name, last_name, age, countrie: f'Sus datos completos son {name.title()} {last_name.title()} tiene {age} años y vive en {countrie.title()}'

text = datos_completos('camilo', 'mejia', 35, 'colombia')
print(text,'\n')

# Now if  you want to call a lambda function, you will use an approach known as immediately invoking the function. That looks like this:

(lambda x : x * 2)(3)
print((lambda x : x * 2)(3)) # 6
# or
print((lambda x, y: x + y)(3,2),'\n') # 5

# Filter()

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filter(lambda x: x % 2 == 0, list1)

# The result is always filter object so I will need to convert it to list using list()

print(list(filter(lambda x: x % 2 == 0, list1)),'\n') # [2, 4, 6, 8, 10]

# Map()

list1 = [2, 3, 4, 5]
print(list(map(lambda x: pow(x, 2), list1)),'\n') # [4, 9, 16, 25]