def target_sum(arr, target):

    values = {}
    result = []

    for i in range(len(arr)):

        if arr[i] in values:
            result.append(values[arr[i]])
            result.append(i)
        else:
            diff = target - arr[i]
            values[diff] = i
    return result


print(target_sum([2, 7, 11, 15], 9))

