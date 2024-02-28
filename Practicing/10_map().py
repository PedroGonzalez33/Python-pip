# map sintaxis: map(function, iterable[, iterable1, iterable2,..., iterable_N])

# example with lambda

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers,'\n') # [1, 4, 9, 16, 25]

# example with funtions 1

def square(x):
    return x ** 2
squared_numbers = list(map(square, numbers))
print(squared_numbers,'\n') # [1, 4, 9, 16, 25]

# example with funtions 2

def myfunc(n):
  return len(n)

x = list(map(myfunc, ('apple', 'banana', 'cherry'))) # [5, 6, 6]
print(x,'\n')

# Hay que tener precaucion al trabajar con map sobre diccionarios ya que al modificar un atributo de un diccionario puedes estar modificando todo el array original y no generando uno nuevo lo cual puede que no sea lo que estas esperando

# Map con diccionario

# transformar una lista de diccionario a una lista de numeros
items = [
  {
    'product':'camisa',
    'price':100
  },
  {
    'product':'pantalon',
    'price':300
  },
  {
    'product':'vestido',
    'price':150
  },
  {
    'product':'chaqueta',
    'price':400
  }
]

prices = list(map(lambda item: item['price'], items))
print(prices)
# --> [100, 300, 150, 400] # lista de precios

# agregar un nuevo atributo a la lista de diccionarios
def add_taxes(items):
  items['taxes'] = items['price'] * .19
  return items
  
new_items = list(map(add_taxes, items))
print(new_items)
""" --> [{'product': 'camisa', 'price': 100, 'taxes': 19.0}, 
		 {'product': 'pantalon', 'price': 300, 'taxes': 57.0}, 
		 {'product': 'vestido', 'price': 150, 'taxes': 28.5}, 
		 {'product': 'chaqueta', 'price': 400, 'taxes': 76.0}]
"""
# el array original es modificado
print(items)
""" --> [{'product': 'camisa', 'price': 100, 'taxes': 19.0}, 
		 {'product': 'pantalon', 'price': 300, 'taxes': 57.0}, 
		 {'product': 'vestido', 'price': 150, 'taxes': 28.5}, 
		 {'product': 'chaqueta', 'price': 400, 'taxes': 76.0}]}
"""