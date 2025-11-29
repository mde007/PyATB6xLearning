# Numbers in a list within a given range

rows = int(input("Enter number of rows of the ML list: "))
cols = int(input("Enter number of columns of the ML list: "))
#line = []

# multidimensional_list = [[0 for _ in range(cols)] for _ in range(rows)]
# print(multidimensional_list)

multidimensional_list = []
for i in range(rows):
    line = []
    for j in range(cols):
        line.append(0)
    multidimensional_list.append(line)
print("The Multidimensional List formed: ",multidimensional_list)