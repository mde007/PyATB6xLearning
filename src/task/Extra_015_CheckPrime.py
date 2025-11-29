# Write a Python program to check if a number is a prime number
"""

n = int(input("Enter the number of fibonacci sequence to be displayed: "))
a, b = 0, 1

if n <= 0:  # Check if n is less than 0
    print("Enter a valid input")
elif n == 1:  # Check if n is equal to 1
    print("Fibonacci series: ", a)
else:
    print("Fibonacci series: ")
    print(a, end=" ") # print first term
    print(b, end=" ")  # print second term
    for i in range(3, n + 1): # print subsequent terms
        c = a + b
        print(c, end=" ")
        a = b
        b = c

"""