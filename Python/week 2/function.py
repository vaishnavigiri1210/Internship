# Function No Arguments

def hello():
    print("Hello, Welcome to Python")

hello()

# Function with Arguments

def add(a, b):
    print(a + b)

add(5, 3)

# Function with Return Value

def multiply(x, y):
    return x * y

result = multiply(4, 5)
print(result)

# function with args i.e arbitarary arguments (in tuple form and infinite arguments can be passed)
# allows you to pass any number of positional arguments to a function.
def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)

my_function("GPP", "IT", "MITU")

# function with kwargs i.e keyword arguments (in dictionary form and infinite arguments can be passed)
# allows you to pass any number of keyword arguments (name-value pairs) to a function.
def my_function(**kwargs):
  print("Type:", type(kwargs))
  print("Name:", kwargs["name"])
  print("Age:", kwargs["age"])
  print("All data:", kwargs)
my_function(name = "Vaishu", age = 20, city = "Pune")

# function with both args and kwargs
def my_function(*args, **kwargs):
  print("Type of args:", type(args))
  print("First argument:", args[0])
  print("Type of kwargs:", type(kwargs))
  print("Name:", kwargs["name"])
  print("All arguments:", args)
  print("All keyword arguments:", kwargs)
my_function("GPP", "IT", name = "Vaishu", age = 20)

# function decorators
def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@my_decorator       #greet = my_decorator(greet)
def greet():
    print("Hello")

greet()

# Lambda Function
x=lambda a,b,c: a+b+c
print(x(5,3,2))
# Use that function definition to make a function that always doubles the number you send in:
def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))

# Lambda with Built-in Functions
# map()
num=[1,2,3,4,5]
squared=list(map(lambda x: x**2, num))
print(squared)

# filter()
num=[1,2,3,4,5,6,7,8,9,10]
even=list(filter(lambda x: x%2==0, num))
print(even)

# reduce()
from functools import reduce
num=[1,2,3,4,5] 
product=reduce(lambda x,y: x+y, num)
print(product)

# sorted()
points = [(2, 3), (1, 2), (4, 1), (3, 4)]
sorted_points = sorted(points, key=lambda point: point[1])
print(sorted_points)

# Recursion Function
def factorial(n):
  # Base case
  if n == 0 or n == 1:
    return 1
  # Recursive case
  else:
    return n * factorial(n - 1)

print(factorial(5))

# scope of variables
x=100  # global variable  
def my_function():
    y=200  # local variable
    print("Inside function:", x)  # accessing global variable
    print("Inside function:", y)  # accessing local variable
my_function()
print("Outside function:", x)  # accessing global variable
# print("Outside function:", y)  # This will raise an error as y is not defined outside the function