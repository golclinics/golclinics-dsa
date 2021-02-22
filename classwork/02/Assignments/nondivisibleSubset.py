def nonDivisibleSubset(k, s):
    remainderArray = [0] * k
    
    for i in s:
        remainderArray[i % k] += 1
        
    if remainderArray[0] > 0:
        maxSet = 1
    else:
        maxSet = 0
        
    for x in range(1, (k+1) // 2):
            maxSet += max(remainderArray[x], remainderArray[k-x])
            
    if k % 2 == 0:
            maxSet += min(remainderArray[k // 2], 1)
    
    return maxSet