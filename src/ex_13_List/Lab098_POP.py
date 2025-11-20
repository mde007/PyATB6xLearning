squares = [1, 4, 9, 16, 25]
print(squares)
print(squares.pop())  # Remove and return/prints item removed at index (default last).
print(squares)
print(squares.pop(1))
print(squares)

squares.clear()
print(squares)
squares.extend([1, 2, 3])
print(squares)

# index(element, start, end)
# Returns the index of the first occurrence of the element.
numbers = [10, 20, 30, 20, 40]
print("First: ",numbers.index(20))

print(numbers.count(20))

numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

# reverse() Reverses the list in place.

numbers.reverse()
print(numbers)

# max() / min() / sum() Works for numerical lists.
print(max(numbers))  # 40
print(min(numbers))  # 10
print(sum(numbers))  # 120

# Slicing
print("List: ",numbers)  # [10, 20, 20, 30, 40]
print(numbers[1:4])  # from index of 1 to 3
print(numbers[-1])  # # Last element

print("apple" in numbers) # in function searches the element in the list, returns bool
print(20 in numbers)

# List Creation and Comprehension
# range(1,5) -> list
l = list(range(1, 5)) #list function converts a range of values in a list
print(l)

# Nested Lists
matrix = [[1,2,3], [4,5,6], [7,8,9]]
print(matrix[1][2])

# del statement - Deletes an element by index or the whole list.
print(matrix[0:3])
del matrix[0:3]
print("Del: ",matrix)
