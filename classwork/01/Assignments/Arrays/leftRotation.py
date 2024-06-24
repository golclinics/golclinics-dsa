
def rotLeft(a, d):
    n = int(input())
    for i in range(d):
        tmp = a[0]
        for j in range(n-1):
            a[j] = a[j+1]
        a[n-1] = tmp
    
    return a
