#Task - print function args
print("Moumita", 123, "Amit", "John", sep='*', end="\n")
#****************************************************
#Task - Take a input from a user and print the table

print("Enter a number to print its table: ")
num = int(input())

print("The table is as follows:")
for i in range(1, 11):  #range starts from 1 but ends 1 value before end i.e.10
    print(f"{num} x {i} = {num * i}")
    #The f-string allows you to combine text and variables or expressions easily in a single print statement.

print("\n")
#****************************************************
#Task - List the all the functions available for the String Data Type
sample=" " # Create a sample string
methods= dir(sample) # Use the dir() function to get all attributes and methods of the string object

#Print all functions
print("All methods available for String data type:\n")
for func in methods:
    print(func)
print("\n")

# Print only the methods (filtering out special methods that start with '__')
print("The filtered methods for String data type:\n")
for func in methods:
    if not func.startswith("__"):
        print(func)
