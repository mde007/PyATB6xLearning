"""✅ Triangle Classifier:
Write a program that classifies a triangle based on its side lengths.
Given three input values representing the lengths of the sides,
determine if the triangle is equilateral (all sides are equal),
isosceles (exactly two sides are equal), or scalene (no sides are equal).

Use an if-else statement to classify the triangle.
3 Input
side 1, side 2 and side 3
output - Eq, Iso, Scalene -
Eq. = side 1 == side 2 = side 3
"""

a = int(input("Enter length of the first side of a triangle: "))
b = int(input("Enter length of the second side of a triangle: "))
c = int(input("Enter length of the third side of a triangle: "))

if (a + b > c) and (b + c > a) and (c + a > b):
    if a == b == c:
        print("Equilateral triangle")
    elif (a == b) or (b == c) or (c == a):
        print("Isosceles triangle")
    else:
        print("Scalene triangle")
else:
    print("We cant draw a triangle with given lengths.")
