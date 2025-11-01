# Problem  Find the Max between 3 numbers

# Logic Building

# User inputs - num1, num2, num3 -> int
# O/p -> int or String with max number .


num1 = int(input("Enter the num1:\n"))  # 5 , # 10
num2 = int(input("Enter the num2:\n"))  # 3 , # 12
num3 = int(input("Enter the num3:\n"))  # 2 , # 11

# 5 > 3 and 5 >2 ->  5
# num1 > num2 and num1 > num3 -> num1
# num2 > num1 nad num2 > num3 -> num2
# num3 - max
"""
if num1 >= num2 and num1 >= num3:
    print("Max", num1)
elif num2 >= num3 and num2 >= num1:
    print("Max", num2)
else:
    print("Max", num3)
"""
#Use the ternary operator to find the maximum of three numbers entered by the user
max_num = num1 if (num1>num2 and num1>num3) else (num2 if (num2>num3 else num3)
print("Max of the numbers: ", max_num)