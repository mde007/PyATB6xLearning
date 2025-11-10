# Print even numbers between 1 and 20

a = int(input("Enter the number: "))
fact = 1

if a == 0:
    print(f"Factorial of {a}: {fact}")
elif a < 0:
    print("ERROR: Factorial is undefined for negative integers.")
else:
    for i in range(1, a + 1):
        fact = fact * i
    print(f"The factorial of {a} using a loop is: ", fact)
