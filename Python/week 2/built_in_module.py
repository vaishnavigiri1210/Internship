# built-in modules
import math
import random
import datetime
import sys
import platform

# math module
num = 25
print("Square root of", num, "is:", math.sqrt(num))
print("Value of pi:", math.pi)

# random module
random_num = random.randint(1, 10)
print("Random number between 1 and 10:", random_num)

# datetime module
current_date_time = datetime.datetime.now()
print("Current date and time:", current_date_time)
print("Current year:", current_date_time.year)

# sys module
print("Python version:", sys.version)
print("Command line arguments:", sys.argv)

#platform module
print("Platform:", platform.system())

# dir() function to list attributes and methods of a module
print(dir(platform))
# print(dir(math))
# dir module can be used on all built-in modules as well as user-defined modules

print("Program executed successfully")