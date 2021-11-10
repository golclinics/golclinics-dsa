def reverse(arr):
    # Creates a new array
    # return [arr[i] for i in range(len(arr)-1, -1, -1)]
    for i in range(len(arr)//2):
        arr[i], arr[~i] = arr[~i], arr[i]
    return arr

# Example 1
print(reverse([1, 2, 5, 6]))

# Example 2
print(reverse([]))

# Example 3
print(reverse([1]))
