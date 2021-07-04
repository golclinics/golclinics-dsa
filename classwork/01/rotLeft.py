def rotLeft(a, d):

    # shift d times to the left (d is in the range of 1 - n)
    n = len(a)
    k = d % n

    res = a[:]
    for i in range(n):
        res[i-k] = a[i]
    
    return res

# driver code
print(rotLeft([1,2,3,4,5], 1))