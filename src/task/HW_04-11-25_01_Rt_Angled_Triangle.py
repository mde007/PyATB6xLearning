"""✅ Grade Calculator:
Write a program to print a right angled triangle with *
*

**

***
"""
def lt_align_triangle(rows):
    for i in range(1, rows+1):
        for j in range(1, i+1):
            print("*", end='') # Print asterisks
        print("\n")

def rt_align_triangle(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i), end="")  # Print leading spaces
        print("*" * i) # Print asterisks

n= int(input("Enter number of rows: "))
rt_align_triangle(n)
lt_align_triangle(n)

