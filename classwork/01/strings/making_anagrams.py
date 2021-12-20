# O(a + b) 
# Using dictionary beacause of fast operations at the ends - O(1) best case
def makeAnagram(a, b):
    charsDict = {}
    num = 0
    
    for char in a:
        if char in charsDict.keys():
            charsDict[char] += 1
        else:
            charsDict[char] = 1
    
    for char in b:
        if char in charsDict.keys():
            charsDict[char] -= 1
        else:
            charsDict[char] = -1
    
    for value in charsDict.values():        
        num += abs(value)
        
    return num
