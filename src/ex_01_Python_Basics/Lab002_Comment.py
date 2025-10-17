# This is Comment
# This code will not be executed.
# print(2+2)
print(2+2)

def calculate_area(length, width):
    """
    Calculates the area of a rectangle.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The calculated area of the rectangle.
    """
    return length * width

#Accessing the doc string
print(calculate_area.__doc__)
