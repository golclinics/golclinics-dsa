def minimumSwaps(arr):
    # create a dictionary which holds value index pairs of our array

    swaps = 0

    for i in range(len(arr)):
        pos = i+1

        while pos != arr[i]:
            val = arr[i]
            arr[i], arr[val - 1] = arr[val - 1], arr[i]
            swaps += 1

    return swaps

print(minimumSwaps([1,3,5,2,4,6,7]))