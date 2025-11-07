#Task - Take an input from a user and print the table

print("Enter a number to print its table: ")
num = int(input())

print("The table is as follows:")
for i in range(1, 11):  #range starts from 1 but ends 1 value before end i.e.10
    print(f"{num} x {i} = {num * i}")
    #The f-string allows you to combine text and variables or expressions easily in a single print statement.

print("\n")