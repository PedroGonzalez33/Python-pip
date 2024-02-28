import functools

numbers = [1,5,3,-1]

def max_num(max,items):
  if max < items:
    max = items
  return max

result = functools.reduce(max_num, numbers)
print(result)


lis = [1, 3, 5, 6, 2]

# using reduce to compute sum of list

print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a+b, lis))

# using reduce to compute sum of list with initializer

print("The sum of the list elements is with initializer is: ", end="")
print(functools.reduce(lambda a, b: a+b, lis,3))