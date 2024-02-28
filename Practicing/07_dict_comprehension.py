import random

# dict comprehension

# clasic
numbers = {}
for i in range(1, 6):
  numbers[i] = i * 3
print(numbers)

# dict comprenhension
numbers_v2 = {i: i * 3 for i in range(1, 6)}
print(numbers_v2)

print("-" * 35)

countries = ["ar", "bol", "col", "mex", "pe"]

# clasic
population = {}
for country in countries:
  population[country] = random.randint(50, 100)
print(population)

# dict comprehension
population_v2 = {country: random.randint(50, 100) for country in countries}
print(population_v2)

print("-" * 35)

names = ["Dolores", "Jashin", "Mifune", "Minos"]
ages = [21, 19, 23, 22]

# clasic
person = {}
for i in range(len(names)):
  person[names[i]] = ages[i]
print(person)

# dict comprehension
person_v2 = {names[i]: ages[i] for i in range(len(names))}
print(person_v2)

# zip
"""a = zip(names, ages)
b = list(zip(names, ages))
c = tuple(zip(names, ages))"""
d = dict(zip(names, ages))

"""print(a)
print(b)
print(c)"""
print(d)

# My test
teams = ['Madrid', 'city', 'unknow']
matches = ['l', 'w']
dict = dict(zip(teams, matches))

total = {k : ('3' if v == 'w' else '1') for k,v in dict.items()}
print(total)

# Conditionals
#-----------Dict comprehension con coniciones------------

#Crear un dict comprehension con una lista
import random 
countries = ['colombia', 'bolivia', 'mexico']

population = { country: random.randint(1, 100) for country in countries}
print(population)

#crear un dict comprehension con una condicion
#paises con poblacion mayor a 30
result = {country: population for (country, population) in population.items() if population > 30}
print(result) 

#dict comprehension de las vocales de una oracion
text = 'Hola nuevo mundo'
unique = { c: c.upper() for c in text if c in 'aeiou'}
print(unique)