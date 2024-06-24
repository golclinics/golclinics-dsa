# O(n) time complexity
# O(n) space complexity


def reverse1(a):
    i = 0
    j = len(a)
    b = a[:]

    while j > 0:
        #b.append(a[j - 1]) -> not efficient
        b[i] = a[j - 1]
        i += 1
        j -= 1

    return b

# O(n) time complexity
# O(1) space complexity


def reverse2(a):
    temp = None
    i = 0
    j = len(a)
    half_len = int(j/2)

    for _ in range(half_len):
        temp = a[i]
        a[i] = a[j - 1]
        a[j - 1] = temp
        i += 1
        j -= 1

    return a


print(reverse1([1, 2, 3, 4]))
print(reverse2([1, 2, 3, 4, 5]))
