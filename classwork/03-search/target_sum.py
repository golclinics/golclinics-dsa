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

def target_sum_binary_search(arr, target):
    n = len(arr)
    l = 0
    r = n - 1

    mid = l + (r-l)//2
    twosum = arr[l] + arr[mid]
    if twosum == target:
        return [l, mid]
    elif twosum > target:
        r = mid
    elif twosum < target:
        l = mid+1
        
    return target_sum_binary_search(arr[l:r])





print(target_sum([2, 7, 11, 15], 9))
print(target_sum_binary_search([2, 7, 11, 15], 9))

