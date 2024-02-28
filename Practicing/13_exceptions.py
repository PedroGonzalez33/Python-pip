# Can be a general exception like this

mytuple = ("apple", "banana", "cherry")

try:
  print(next(mytuple))
except Exception:
  print('error\n')

# or can be an specific exception like this

try:
  print(0/0)

except ZeroDivisionError as error:
  print(error,': You cant divide for 0\n')

# We can also make our own exceptions 

age = 10 

try:
  if age < 18:
    raise Exception('No se permiten menores de edad')
    
except Exception as error:
  print(error,'\n')

# there are more declarations in try/except command

try:
    num_one = 1 
    num_two = 2
    sum = num_one + num_two #this statement throws an exception
    print(f"Suma: {sum}")


except TypeError as type_exception:
    print("A TypeError has happend, error: ", type_exception)


except ValueError:
    print("A ValueError has happend")


except Exception as exception:
    print("An exception has happend, error: ", exception)


else:
    print("The code was runned well")


finally:
    print("This code will run en every time")