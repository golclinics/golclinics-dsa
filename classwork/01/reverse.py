
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

# Both iterative and recursive approach are O(N) time and O(N) space complexity


# 1. Reverse Array In-place
# Write a function reverseArray(A) that takes in an array A and reverses it, without using another array
#  or collection data structure
# in-place.

# Example:

# A = [10, 5, 6, 9] reverseArray(A) A // [9, 6, 5, 10]
# Share the Github link to your solution.

def reverse_inplace(arr):

    n = len(arr)

    mid = n // 2

    if n % 2 == 0:
        left = mid - 1
        right = mid
    else:
        left = mid - 1
        right = mid + 1
    
    for _ in range(mid):
        arr[left], arr[right] = arr[right], arr[left]
        left -= 1
        right += 1

    return arr


# driver code
print(reverse([1,2,3,4,5]))
print(reverse_recursive([1,2,3,4,5]))
print(reverse_inplace([1,2,3,4,5]))
