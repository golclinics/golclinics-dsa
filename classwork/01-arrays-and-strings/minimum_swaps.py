def minimumSwaps(arr):
    swaps = 0
    tmp = {}

    for i, val in enumerate(arr):
        import pdb
        pdb.set_trace()
        tmp[val] = i

    for i in range(len(arr)):
        if arr[i] != i+1:
            swaps += 1
            t = arr[i]
            arr[i] = i+1
            arr[tmp[i+1]] = t

            tmp[t] = tmp[i+1]

    return swaps