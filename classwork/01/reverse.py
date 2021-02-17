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


def reverse_two(array):
    """
    Returns the reverse of the given array
    O(n) T
    O(1) S
    """
    if len(array) == 0:
        return array
    else:
        for i in range(0, (len(array) // 2)):
            array[i], array[-i-1] = array[-i-1], array[i]

        return array


array = [1, 2, 3, 4, 5, 6, 7]

print(reverse(array))
print(reverse_two(array))
