#Transformate float to integer
print('Transformate float to integer')
a = 3.5
a = int(a)
print('Transformation from float to integer of a is: ', a) 
print(type(a)) # <class int> / out: 3

#Transformate float to string
print('Transformate float to string')
b = 3.5 # <class 'float'>
b = str(b)
print('Transformation from float to string of b is: ' + b) 
print(type(b)) # <class 'str'> / out: 3.5

#Transformate string to float
print('Transformate string to float')
c = "35.5"
c = float(c)
print('Transformation from string to float of c is: ', c)
print(type(c)) # <class 'float'> / out: 35.5

#Transformate string to integer
print('Transformate string to integer')
d = "3" # <class 'str'>
d = int(d)
print('Transformation from string to integer of d is: ', d)
print(type(d)) # <class 'int'> / out: 3

#Transformate integer to string
print('Transformate integer to string')
e = 10
e = str(e)
print('Transformation from integer to string of e is: ', e)
print(type(e)) # <class 'str'> / out: 10 

#Transformate to a list
print('Transformate to a list')
f = {1, 2, 3}
g = list(f)
print(f, 'type: ', type(f)) # <class 'set'>
print(g, 'type: ', type(g)) # <class 'list'>

#Transformate to a set
print('Transformate to a set')
h = ["Python", "Mola"]
i = set(h)
print(h, 'type:', type(h)) # <class 'list'>
print(i, 'type: ', type(i)) # <class 'set'>