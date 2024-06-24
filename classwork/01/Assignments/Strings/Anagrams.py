def makeAnagram(a, b):
    counter = 0
    charArrayA = list(a)
    charArrayB = list(b)
    
    for i in range(len(a)):
        for j in range(len(b)):
            if(charArrayA[i] == charArrayB[j]):
                charArrayB[j] = 0
                counter += 1            
       
    totalSum = len(a) + len(b) - 2 * (counter)
    
    return totalSum    
