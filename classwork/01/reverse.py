

def reverse(A):
    n = len(A)
    r_list = A[:] # clone the original array
   
    j = 0
    for i in range(n-1, -1, -1):
        r_list[j] = A[i]
        j += 1

    return r_list

# driver code
print(reverse([1,2,3,4,5]))