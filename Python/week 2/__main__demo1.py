def message():
    print("Hello Python")

if __name__ == "__main__":
    print("THIS IS THE DEMO OF __MAIN__")
    message()
# __name__ == "__main__" → TRUE (file is run directly)
# So both lines inside the block execute:
# print("THIS IS THE DEMO OF __MAIN__")
# message() → prints Hello Python

# this statement will be run in both __main__demo1.py and _main__demo2.py 
# because this statement is outside of __main__ block
print("my name is:", __name__)     