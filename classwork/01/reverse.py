def reverse(array):
    """
    Returns the reverse of the given array
    O(n) TS
    """
    rev_array = []
    if len(array) == 0:
        return array
    else:
        for i in range(len(array)-1, -1, -1):
            rev_array.append(array[i])

        return rev_array


array = [1, 2, 3, 4, 5, 6, 7]

print(reverse(array))
