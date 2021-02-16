def reverse(arr):
    return [arr[i] for i in range(len(arr)-1, -1, -1)]

print(reverse([1, 2, 5, 6]))
print(reverse([]))
print(reverse([1]))
