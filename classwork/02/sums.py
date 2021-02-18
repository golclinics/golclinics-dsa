# O(N) Time Complexity
def combine_index(arr, k):
    addition_dict = dict()
    for i in range(len(arr)):
        el = arr[i]
        if el in addition_dict:
            return i, addition_dict[el]
        addition_dict[k - el] = i

print(combine_index([2, 7, 11, 15], 9))
print(combine_index([2, 3, 4], 6))
