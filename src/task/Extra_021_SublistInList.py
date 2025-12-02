# Check for sub_list' is a contiguous sublist of 'main_list'

def sublist_exists(list1, list2):
    a=0
    for items in list2:
        if items in list1:
            a+=1
    if a == len(list2):
        return True
    else:
        return False

main_list = ["aa", "bcb", "de", "fgh", "cccc", "setts"]
#sub_list = []
#sub_list = ["a", "bb"]
sub_list = ["de", "setts", "cccc", "fgh"]

if not sub_list:
    print("Sublist is empty")
elif not sublist_exists(main_list, sub_list):
    print("No match")
else:
    print("Sublist exists in the list")