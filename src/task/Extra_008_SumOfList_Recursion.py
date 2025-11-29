# Sum of List: Calculate the sum of all elements in a list using recursion

""" Normal way using for loop
def sum_func(list1):
    sum_list = 0
    for element in list1:
        sum_list += element
    print(sum_list)

my_list = [1, 2, 3, 4, 5.6, 6]
sum_func(my_list)
"""

def recursive_list_sum(elements, x):
    if x == 0: #empty list scenario
        return 0
    else:
        return elements[x-1] + recursive_list_sum(elements, x-1)

my_list = [1, 2, 3, 4, 5.6]
n = len(my_list)
total_sum = recursive_list_sum(my_list, n)
print(f"The sum of the list elements is: {total_sum}")
