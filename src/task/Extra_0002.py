#Use the ternary operator to find the maximum of three numbers entered by the user
num1 = int(input("Enter first integer: \n"))
num2 = int(input("Enter second integer: \n"))
num3 = int(input("Enter third integer: \n"))

max_num = num1 if (num1>num2 and num1>num3) else (num2 if num2>num3 else num3)
print("Max of the numbers: ", max_num)