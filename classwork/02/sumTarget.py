
#O(n^2) time complexity
#O(1) space complexity


def target_sum(arr, target):
    len_a = len(arr)
    sum_arr = None
    for i in range(len_a):
        for j in range(i + 1, len_a):
            sum_a = arr[i] + arr[j]

            if sum_a == target:
                sum_arr = [i, j]
    return sum_arr


print(target_sum([2, 7, 11, 15], 9))
print(target_sum([2, 3, 4], 6))
