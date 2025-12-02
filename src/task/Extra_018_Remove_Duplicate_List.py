# Write a Python program to remove duplicates from list

def remove_duplicates(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

#my_list = ["aa", "bcb", "de", "bcb", "cccc", "aa", "setts"]
my_list = [1,2,3,4,3,2,1]
print(f"Original list: {my_list}")
print("List after removing duplicates (using loop): ", remove_duplicates(my_list))