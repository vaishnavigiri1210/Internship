# built-in modules
import math
import random
import datetime
import sys

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

print("Program executed successfully")