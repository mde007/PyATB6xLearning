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
