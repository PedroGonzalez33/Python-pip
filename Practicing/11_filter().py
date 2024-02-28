people = [
  {
    'name' : 'Pedro',
    'country': 'Colombia',
    'age' : 18,
    'course' : 'developer'
  },
  {
    'name' : 'Juan',
    'country': 'Perú',
    'age' : 17,
    'course' : 'UX'
  },
  {
    'name' : 'Carlos',
    'country': 'Chile',
    'age' : 31,
    'course' : 'Diseño'
  },
  {
    'name' : 'Ana Maria',
    'country': 'Colombia',
    'age' : 25,
    'course' : 'Tester'
  }
]

# filter the person from colombia, older than 18 and it's a developer

person_selected = list(filter(lambda postulates : postulates['country'] == 'Colombia' and postulates['age'] >= 18 and postulates['course'] == 'developer', people))

print(person_selected, '\n')

print(people)