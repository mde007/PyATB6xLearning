# Write a Python program to count the number of strings in a list where
# the string length is 2 or more and the first and last characters are the same

def count_strings(list1):
    c = 0
    for elements in list1:
        if len(elements) > 1 and elements[0] == elements[-1]:
            c += 1
    return c


my_list = ["aa", "bcb", "de", "fgh", "cccc", "setts"]
print("Count is: ", count_strings(my_list))
