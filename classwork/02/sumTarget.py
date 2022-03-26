def target_sum(arr, target):
    len_a = len(arr)
    sum_arr = None
    for i in range(len_a):
        for j in range(i + 1, len_a):
            sum_a = sum(arr[:i + 1])
            sum_b = sum_a + arr[j]

            if sum_b == target:
                sum_arr = [*range(i + 1), j]
    return sum_arr


print(target_sum([2, 7, 11, 15], 9))
print(target_sum([2, 3, 4], 6))
