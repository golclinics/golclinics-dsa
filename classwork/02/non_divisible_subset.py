def nonDivisibleSubset(k, s):
    count = [0] * k

    for i in s:
        remainder = i % k
        count[remainder] +=1
    
    result = min( count[0] , 1)         

    if k % 2 == 0:
        result += min(count[k//2] ,1 )

    for i in range( 1 , k^2-1):    
        if i != k - i:       
            result += max(count[i] , count[k-i])
    return result