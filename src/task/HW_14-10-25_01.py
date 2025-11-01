# Write a Python program to calculate the area of a triangle using the formula
# Area = 1/2 * Base * Height
# Take Base=10, Height=5, print result using Arithmetic operators


b = float(input("Enter the base: "))
h = float(input("Enter the height: "))

def cal_area (Base=10.0, Height=5.0):
    a = 1/2 * Base * Height
    print("Area of the triangle: ", a)

cal_area(b, h)