# Basic HOF

def increment(x):
  return x + 10

increment_v2 = lambda x: x + 10

def hof(x, func):
  return x + func(x)

result = hof(20, increment)
# 20 + (20 + 10)
print(result,'\n') # 50

# HOF with lambda

function = lambda x, fuct: x**fuct()

result = function(2, lambda : 5) 
print(result,'\n') # 32

# Functions as objects
# Python program to illustrate functions 
# can be treated as objects 
def shout(text): 
    return text.upper() 
    
print(shout('Hello')) # HELLO
    
# Assigning function to a variable
yell = shout 
    
print(yell('Hello'),'\n') # HELLO

# Passing Function as an argument to other function
# Python program to illustrate functions 
# can be passed as arguments to other functions 
def shout(text): 
    return text.upper() 
    
def whisper(text): 
    return text.lower() 
    
def greet(func): 
    # storing the function in a variable 
    greeting = func("Hi, I am created by a function \
    passed as an argument.") 
    print(greeting)  # HI, I AM CREATED BY A FUNCTION     PASSED AS AN ARGUMENT. / hi, i am created by a function     passed as an argument.
    
greet(shout) 
greet(whisper)

# Returning function
# Python program to illustrate functions
# Functions can return another function
	
def create_adder(x):
	def adder(y):
		return x + y
	
	return adder
	
add_15 = create_adder(15)
	
print('\n',add_15(10)) # 25