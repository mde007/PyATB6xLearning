# Print numbers from 10 down to 1

a = int(input("Enter the number: "))
fact=1

if a==0:
    print(f"Factorial of {a}: 1")
elif a<0:
    print("Factorial is only defined for non-negative integers.")
else:
    for i in range(1, a+1):
        fact = fact*i
    print(f"The factorial of {a} using a loop is: ",fact)

