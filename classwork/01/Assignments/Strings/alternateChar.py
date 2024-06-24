def alternatingCharacters(s):
    q = int(input())
    for _ in range(q):
        counter = 0
        for i in range(len(s)-1):
            if(s[i] == s[i+1]):
                counter += 1
        
    return counter
