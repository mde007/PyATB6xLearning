""" Write a Python program to get the Fibonacci series between 0 to 50
# 0,0+1, 0+1+1,
# n = 7
# 0, 1, 2, 3, 5, 8, 13
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

