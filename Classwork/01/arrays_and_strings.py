# My First Solution

def reverse(A):
  return A[::-1]


# Example 1
print(reverse([1, 2, 5, 6]))

# Example 2
print(reverse([]))

# Example 3
print(reverse([1]))







# My second solution

def Reverse(A):
    
    if len(A) == 0: return []
    else: return [A.pop()] + Reverse(A)


# Example 1
print(Reverse([1, 2, 5, 6]))

# Example 2
print(Reverse([]))

# Example 3
print(Reverse([1]))
