def target_sum(arr, target):
    sum_indices = []

    for i in range(len(arr)):
        for j in range(i, len(arr) - 1):
            if arr[i] + arr[j+1] == target:
                sum_indices = [i, j + 1]

                break
        else:
            continue
        break

    return sum_indices


if __name__ == '__main__':
    print(target_sum([2, 4, 11, 8], 12))
    print(target_sum([2, 3, 4], 6))
