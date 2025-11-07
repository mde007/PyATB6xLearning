"""Create a program that takes two numbers as input and
prints whether the first number is greater than, less than, or equal to the second number"""

num1 = int(input("Enter first integer: \n"))
num2 = int(input("Enter second integer: \n"))

if num1 > num2:
    print("First num is greater")
elif num1 == num2:
    print("Both numbers are equal")
else:
    print("Second num is greater")