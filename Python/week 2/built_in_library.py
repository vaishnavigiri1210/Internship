# Importing libraries
import math
import random
import datetime
import sys
import os
import statistics
import time

# math library
num = 25
print("Square root of", num, ":", math.sqrt(num))

# random library
rand_num = random.randint(1, 10)
print("Random number between 1 and 10:", rand_num)

# datetime library
now = datetime.datetime.now()
print("Current date and time:", now)
print("Current year:", now.year)

# statistics library
data = [10, 20, 30, 40, 50]
print("Mean of data:", statistics.mean(data))

# os library
print("Current working directory:", os.getcwd())

# sys library
print("Python version:", sys.version)

# time library
print("Waiting for 1 second...")
time.sleep(1)

print("Program executed successfully")
