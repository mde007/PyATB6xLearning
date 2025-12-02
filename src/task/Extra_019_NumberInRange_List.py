# Numbers in a list within a given range

def num_in_list(input_list, a, b):
    unique_list = []
    for item in input_list:
        if a <= item <= b:
            unique_list.append(item)
    if not unique_list:
        print("No items in the range")
    else:
        print("The list of items in the given range: ",unique_list)

my_list = [100, 20, 30, 80, 77, 54, 1]
start_pos = int(input("Enter the start of the range: "))
end_pos = int(input("Enter the end of the range: "))

if start_pos <= end_pos:
    num_in_list(my_list, start_pos, end_pos)
else:
    print("Start position should be less than equal to end position. Please retry!")
