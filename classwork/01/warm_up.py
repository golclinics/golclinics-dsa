# Space complexity O(1)

def reverse_helper(A, start_index, end_index):
    while start_index < end_index:
        # Python Clever
        # A[start_index], A[end_index] = A[end_index], A[start_index]
        
        # Generic - Using a temporary variable for switch
        temp = A[start_index]
        A[start_index] = A[end_index]
        A[end_index] = temp

        start_index += 1
        end_index -= 1

    return A

def reverse(A):
    return reverse_helper(A, 0, len(A) - 1)


# Space complexity O(n)

def reverse_arr(A):
    copy_A = [None] * len(A)
    j = 0

    for i in range(len(A) -1, -1, -1):
        copy_A[j] = A[i]
        j += 1


    return copy_A


