""" Write a Python program to get the Fibonacci series between 0 to 50
# 0, 1, 2, 3, 5, 8, 13
"""
def fib_series_upto_n(limit):
    fib_numbers = []
    a, b = 0, 1

    while a <= limit:
        fib_numbers.append(a) #0,
        a, b = b, a + b
    return fib_numbers

n = int(input("Enter the limit of fib series to show: "))
print(f"Fibonacci series between 0 and {n}:", fib_series_upto_n(n))