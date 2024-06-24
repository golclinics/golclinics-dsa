def hourglassSum(arr):
    result = []
    n = len(arr)

    for i in range(n-2):
        for j in range(n-2):
            total = sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3])
            result.append(total)
    
    return max(result)


arr = [[1, 1, 1, 0, 0, 0],
[0, 1, 0, 0, 0, 0],
[1, 1, 1, 0, 0, 0],
[0, 0, 2, 4, 4, 0],
[0, 0, 0, 2, 0, 0],
[0, 0, 1, 2, 4, 0]]

print(hourglassSum(arr))