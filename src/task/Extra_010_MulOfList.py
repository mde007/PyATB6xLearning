# Write a Python program to multiply all numbers in a list

def mul_func(list1):
    product = 1
    for element in list1:
        if element == 0:
            return 0
        else:
            product *= element
    return product


my_list = [1, 2, 3, 4, 5, 10]
print("Multiplication product of the list elements: ", mul_func(my_list))
