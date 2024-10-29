# Three scenarios when the string is valid
# all the chars occurs the same amount of time, for exampe s = aaabbbcccddd
# one char occurs one more time than all the rest, for example s = aaaabbbcccddd
# one char only occurs one time, while the rest occur the same amount of times, for example s = aaabbbcccd

def isValid(s):
    charsDict = {}

    for char in s:
        if char in charsDict.keys():
            charsDict[char] += 1
        else:
            charsDict[char] = 1

    countDict = {}
    max_count, min_count = charsDict[max(charsDict, key=charsDict.get)], charsDict[min(charsDict,key=charsDict.get)]

    for char,value in charsDict.items():
        if value in countDict:
            countDict[value] += 1
        else:
            countDict[value] = 1

    if len(countDict) == 1:
        return 'YES'
    elif len(countDict) == 2:
        if countDict[max_count] == 1 and max_count - min_count == 1:
            return 'YES'
        elif countDict[min_count] == 1 and min_count == 1:
            return 'YES'

    return 'NO'



# Other initialization of max and min - O(n)
def isValid(s):
    # Go over string and count how many times string occured
    char_dict = {}
    for char in s:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    min_count = char_dict[char]
    max_count = char_dict[char]
    count_dict = {}
    
    for char, value in char_dict.items():
        if value in count_dict:
            count_dict[value] += 1
        else:
            count_dict[value] = 1
        #also update max and min count
        if value < min_count:
            min_count = value
        if value > max_count:
            max_count = value
    
    if len(count_dict) == 1:
        return 'YES'
    elif len(count_dict) == 2:
        if count_dict[max_count] == 1 and max_count - min_count == 1:
            return 'YES'
        elif count_dict[min_count] == 1 and min_count == 1:
            return 'YES'
    return 'NO'
