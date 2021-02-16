def reverse(array):
    """
    Returns the reverse of the given array
    """
    if len(array) == 0:
        return array
    else:
        return array[::-1]


array = [1, 2, 3, 4, 5, 6, 7]

print(reverse(array))
