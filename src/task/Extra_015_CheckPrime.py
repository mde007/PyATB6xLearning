# Write a Python program to check if a number is a prime number

def check_prime(n):
    if n <= 1:
        return False  # Numbers less than or equal to 1 are not prime

    # Iterate from 2 up to the square root of the number
    # We only need to check divisibility up to the square root because if a number
    # has a factor greater than its square root, it must also have a factor
    # smaller than its square root.
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  # If divisible by any number other than 1 and itself, it's not prime
    return True  # If no divisors found, it's prime

# Example usage:
num = int(input("Enter a number to check: "))
if check_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")