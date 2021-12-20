# Python Clever
# Watch out for space complexity since 2 additional list copies are being created
def rotLeft(a, d):
    return a[d:] + a[:d]

# O(n) time complexity, O(1) space complexity
def rotLeft(a, d):
    for i in range(d):
        temp = a.pop(0)
        a.append(temp)
    return a
