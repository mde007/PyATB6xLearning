# Check if two lists are identical.

one_list = ["aa", "bcb", "de", "fgh", "cccc", "setts"]
#two_list = ["aa", "bcb", "de", "fgh", "cccc", "setts"]
two_list = ["setts", "yui", "de"]

def common_element(list1, list2):
    for elements in list1:
        for items in list2:
            if elements != items:
                return False
            else:
                return True

if common_element(one_list, two_list):
    print("Lists are identical")
else:
    print("Lists are not identical")
