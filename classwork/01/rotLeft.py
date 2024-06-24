def rotLeft(a, d):

    # shift d times to the left (d is in the range of 1 - n)
    n = len(a)
    temp = [None for _ in range(n)]
    for i in range(n):
        temp[i-d] = a[i]
    
    return temp

# driver code
print(rotLeft([1,2,3,4,5], 4))