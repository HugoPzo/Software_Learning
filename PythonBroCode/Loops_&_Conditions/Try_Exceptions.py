# +++++++++Try / Exceptions+++++++++

# exception = Events detected during execution that interrupt the flow
#              of a program

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e: # Assign the error to a variable
    print(e) # The error will be printed
    print("You can't divide by zero!!!")
except ValueError as e:
    print(e)
    print(f"Enter only numbers plz!!!")
except Exception as e:
    print(e)
    print("Something go wrong :(")
else: # If there are no exceptions, this part of the code will execute
    print(f"Your result is {result}")
finally: # Whether or not are exception, this code will be executed
    print("This part of the code always will be executed")

