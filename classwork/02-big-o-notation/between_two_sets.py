def getTotalX(a, b):
    maximum_a = max(a)
    minimum_b = min(b)
    count = 0
    for i in range(maximum_a, minimum_b+1):
        if all([i%j==0 for j in a]):
            if all([j%i==0 for j in b]):
                count += 1
    return count