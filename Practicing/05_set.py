# set values don't have key-value, That's how I realize it's a set,(Un conjunto).
set_countries = {'col', 'mex', 'bol'}
print (set_countries)

# if i put a repetitive value the set will delete it.
set_countries2 = {'col', 'mex', 'bol', 'col'}
print (set_countries2) # {'col', 'mex', 'bol'}

# puede ser mixto. El set se ordena solo, lo importante es lo que tengo dentro.
set_types = {1, 'hola', False, 12.12}
print(set_types) # {False, 1, 12.12, 'hola'}

# la podemos crear a partir de un string
set_from_string = set('hoola')
print (set_from_string) # {'a', 'l', 'o', 'h'}

# la podemos crear a partir de una tupla
set_from_tuples = set (('abc','cbv','as','abc'))
print (set_from_tuples) # {'as', 'abc', 'cbv'}

# la podemos crear a partir de una lista
numbers = [1,2,3,1,2,3,4]
set_numbers= set(numbers)
print (set_numbers) # {1, 2, 3, 4}

# si quiero convertir este set único a una lista, lo puedo hacer:
unique_numbers = list(set_numbers)
print (unique_numbers, '\n')


set_countries = {'col', 'mex', 'bol'}

#len() : Devuelve el tamaño del conjunto
size = len(set_countries)
print(size)

#in, permite sabes si un elemento se encuentra enel conjunto, la expresión se evalua como true si el elemento se encuentra enel conjunto y false si el elemento nose encuentra enel conjunto
print('col' in set_countries)
print('pe' in set_countries)

# add(): Añade un elemento al conjunto.
set_countries.add('pe')
print(set_countries)
set_countries.add('pe')
print(set_countries)

# update(): Añade cualquier tipo de objeto iterable como: listas, tuplas
set_countries.update({'ar', 'ecua', 'pe'})
print(set_countries)

# remove(): Elimina un elemento y si este no existe lanza el error “keyError”
set_countries.remove('col')
print(set_countries)
set_countries.remove('ar')

#discard(): Elimina un elemento y si ya existe no lanza ningún error
set_countries.discard('arg')
print(set_countries)
set_countries.add('arg')
print(set_countries)

#pop(): Nos devuelve un elemento aleatorio ylo elimina y si el conjunto está vacío lanza el error “key error”.
print(set_countries.pop())
print(set_countries)

#clear(): Elimina todo el contenido del conjunto
set_countries.clear()
print(set_countries)
print(len(set_countries),'\n')

print('set Methods:')

set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

# unión de los elementos
set_c = set_a.union(set_b)
print(set_c) # {'col', 'mex', 'bol', 'pe'}
print(set_a | set_b)  # {'col', 'mex', 'bol', 'pe'}

# obtener los elementos en común
set_c = set_a.intersection(set_b)
print(set_c) # {'bol'}
print(set_a & set_b)  # {'bol'}

# dejamos sólo los elementos de A
set_c = set_a.difference(set_b)
print(set_c)  # {'col', 'mex'}
print(set_a - set_b)  # {'col', 'mex'}

# es hacer una unión, sin los elementos en común
set_c = set_a.symmetric_difference(set_b)
print(set_c) # {'col', 'mex', 'pe'}
print(set_a ^ set_b) # {'col', 'mex', 'pe'}