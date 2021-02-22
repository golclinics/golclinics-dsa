def getTotalX(a, b):
    count = 0
    
    for i in range(max(a), max(b)+1):
        for k in a:
            if i % k != 0:
                break
        else:
            for l in b:
                if l % i != 0:
                    break
            else:
               count += 1
                    
            
    return count
