"""✅ Grade Calculator:
Write a program to print a right angled triangle with *
*

**

***

****

*****
"""

def print_triangle(rows):
    for i in range(1, rows+1):
        for j in range(1, i+1):
            print("*", end='')
        print("\n")

print_triangle(int(input("Enter number of rows: ")))
