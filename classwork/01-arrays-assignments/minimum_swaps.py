# optimized on time to O(N)
def minimumSwaps(arr):
    index_value = dict(enumerate(arr, 1))
    value_index = {v: k for k, v in index_value.items()}

    count = 0
    for pos in index_value:
        value = index_value[pos]
        if value != pos:
            index = value_index[pos]
            index_value[index] = value
            value_index[value] = index
            count += 1
    return count

print(minimumSwaps([1,3,5,2,4,6,7]))
