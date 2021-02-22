def alternatingCharacters(s):

    result = 0
    for i in range(len(s) - 1): 
        if (s[i] == s[i + 1]): 
            result += 1                         
    return result 