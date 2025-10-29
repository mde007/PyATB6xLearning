# Task for the Today
# Take a 2 input from the user
# Print the Quotient and Remainder
# 15 ->  num1
# 2 -> num2
# Q -> 7
# R -> 1

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

division = num1 / num2 #True division, Result is always float showing fractional part as well
quotient = num1 // num2 #Floor/Integer division, doesnot return fractional part, only shows quotient
remainder = num1 % num2

print(division)
print(quotient)
print(remainder)