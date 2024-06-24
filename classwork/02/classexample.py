# For a number n, find the sum of 1, 2, ....
def sumNumbers(n: int):
    pass

# Quadratic complexity - time complexity increase by a factor of the input size
# O(n ** 2)
def sumNumbers_soln1(n: int):
    total = 0
    for i in range(n):
        for j in range(n):
            total += 1
    return total

# Linear complexity O(n) - as input grows, the time complexity increases by the same value
# Ratio of 1:1
def sumNumbers_soln2(n: int):
    total = 0
    for i in range(n):
        total += 1
    return total

# Constant complexity - time increases by a constant value regardless of the input size
# O(1)
def sumNumbers_soln3(n: int):
    return n * (n-1) + 1        #Fibonacci series

# Best case, average case, worst case