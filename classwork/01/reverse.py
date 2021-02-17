
# iterative approach
def reverse(A):
    n = len(A)
    r_list = A[:] # clone the original array
   
    j = 0
    for i in range(n-1, -1, -1):
        r_list[j] = A[i]
        j += 1

    return r_list

# recursive approach
def reverse_recursive(A):
    
    if len(A) == 0:
        # base case
        return []
    else:
        # recursive case
        return [A.pop()] + reverse_recursive(A)


# driver code
print(reverse([1,2,3,4,5]))
print(reverse_recursive([1,2,3,4,5]))