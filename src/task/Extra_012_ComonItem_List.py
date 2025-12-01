# Write a Python program that takes two lists and returns True
# if they have at least one common member

one_list = ["aa", "bcb", "de", "fgh", "cccc", "setts"]
two_list = ["setts", "yui", "de"]
common_list = []


def common_element(list1, list2):
    for elements in list1:
        for items in list2:
            if elements == items:
                common_list.append(elements)
    if not common_list:
        print("No match found")
    else:
        print("Items common in both lists: ", common_list)


common_element(one_list, two_list)
