

def reverse(A):
    copy_A = A[:]
    j = 0

    for i in range(len(A) - 1, -1, -1):
        copy_A[j] = A[i]
        j += 1
    
    return copy_A

# tests
a = [1, 4, 5, 6]
print(reverse(a))
