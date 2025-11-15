# Create a function which will take the 3 values from the user,
# which are length of the triangle.  side1, side2, side2
# i/p - int side1 == side2 =side3 → isoceles
# o/p = result in string - iso, eq, scalene

def triangle_classify(a, b, c):
    if a == b == c:
        print("Equilateral triangle")
    elif (a == b) or (b == c) or (c == a):
        print("Isosceles triangle")
    else:
        print("Scalene triangle")

s1 = int(input("Enter length of the first side of a triangle: "))
s2 = int(input("Enter length of the second side of a triangle: "))
s3 = int(input("Enter length of the third side of a triangle: "))

if s1>0 and s2>0 and s3>0:
    if (s1+s2>s3) and (s2+s3>s1) and (s3+s1>s2):
        triangle_classify(s1, s2, s3)
    else:
        print("We cant draw a triangle with given lengths.")
else:
    print("Side lengths cant be zero or negative")