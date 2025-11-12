# Create a function which will take a positive number from the user and give square of the number?
# i/o = 3
# o/p = 9

def square_num(a):
    square = pow(a, 2)
    print("Square of the num: ", square)

num = int(input("Enter a positive integer: "))
if num < 0:
    print("Enter only a positive integer!!!")
else:
    square_num(num)
