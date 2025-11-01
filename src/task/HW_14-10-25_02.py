# Write a program to check if a number entered by the user is greater than 100.
# Use ternary operator


a = float(input("Enter the number: "))

print("The num is greater." if a>100 else "The num is equal to 100." if a==100 else "The num is smaller.")