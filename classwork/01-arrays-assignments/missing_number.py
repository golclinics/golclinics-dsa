# Given two arrays of integers, find which elements in the second array are missing from the first array.

# Example
# arr = [7,2,5,3,5,3]
# brr = [7,2,5,4,6,3,5,3]
# The  array is the orginal list. The numbers missing are .
# Notes

# If a number occurs multiple times in the lists, you must ensure that the frequency of that number in both lists is the same. If that is not the case, then it is also a missing number.
# Return the missing numbers sorted ascending.
# Only include a missing number once, even if it is missing multiple times.
# The difference between the maximum and minimum numbers in the original list is less than or equal to .

# constraints
# 1 <= n,m <=2x10^5
# n<=m
# 1 <= brr[i] <=10^4
# max(brr) - min(brr) <= 100
def missingNumbers(arr, brr):
    freq = [0] * 101 # since difference between max an min is 100
    min_val = min(brr) # min value for adjusting to real values

    # increment count of values in original array
    for i in brr:
        freq[i - min_val] += 1

    # decrement count of values in array we are comparing
    for i in arr:
        freq[i - min_val] -= 1

    res = []

    #get frequency counts that are not 0 meaning the arrays are unequal
    for i in range(len(freq)):
        if freq[i] != 0:
            res.append(min_val + i)

    return res

    
print(missingNumbers([1,2,5], [1,2,33,4,5]))
