##################################################################
###################### A R R A Y S ###############################
############ 2D Array - DS ########################################

def hourglassSum(arr):
    maximum = float('-inf')
    for i in range(4):
        for j in range(4):
            hourglass_sum = sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3])
            maximum = max(hourglass_sum, maximum)
    return maximum

############ Arrays: Left Rotation #################################

def rotLeft(a, d):
    # If d > len(a)
    d = d % len(a)
    return a[d:] + a[:d]

############ New Year Chaos ########################################

def minimumBribes(q):
    n = len(q)
    swap = 0
    # Let us count receiving bribes
    for i in range(n):
        if(q[i] - (i + 1) > 2):
            print("Too chaotic")
            return
        if q[i] > (i + 1):
            next
        for j in range(max(0, q[i]-2), i):
            if q[j] > q[i]:
                swap += 1
    print(swap)

############ Minimum Swaps 2 #########################################

def minimumSwaps(arr):
    swaps = 0
    for i in range(len(arr)):
        position = i + 1
        while position != arr[i]:
            value = arr[i]
            arr[i], arr[value-1] = arr[value-1], arr[i]
            swaps += 1
    return swaps

############ Array Manipulation #######################################

def arrayManipulation(n, queries):
    accumulator_dict = dict()
    for query in queries:
        start = query[0]
        end = query[1]
        value = query[2]
        if start not in accumulator_dict:
            accumulator_dict[start] = 0
        if (end + 1) not in accumulator_dict:
            accumulator_dict[end + 1] = 0
        accumulator_dict[start] += value
        accumulator_dict[end + 1] -= value
    accumulationSum = 0
    maximum = float('-inf')
    for key in sorted(accumulator_dict.keys()):
        accumulationSum += accumulator_dict[key]
        maximum = max(accumulationSum, maximum)
    
    return maximum


#########################################################################
########################## S T R I N G S ################################
############ Strings: Making Anagrams ####################################

def makeAnagram(a, b):
    counter = [0 for _ in range(26)]
    for char in a:
        counter[ord('a')-ord(char)] += 1
    for char in b:
        counter[ord('a')-ord(char)] -= 1
    sums = 0
    for count in counter:
        sums += abs(count)
    return sums

############ Alternating Characters ######################################

def alternatingCharacters(s):
    current_char = s[0]
    deletions = 0
    for i in range(1, len(s)):
        if s[i] == current_char:
            deletions += 1
        else:
            current_char = s[i]
    return deletions

############ Sherlock and the Valid String #################################

def isValid(s):
    counter = [0 for _ in range(26)]
    counter_dict = dict()
    length = 0
    for char in s:
        counter[ord('a') - ord(char)] += 1
    
    for count in counter:
        if count != 0:
            if count not in counter_dict:
                length += 1
                counter_dict[count] = 1
                if length > 2:
                    return "NO"
            else:
                counter_dict[count] += 1
    
    if length == 1:
        return "YES"
    
    if 1 in counter_dict and counter_dict[1] == 1:
        return "YES"
    
    maximum_letters = max(list(counter_dict))
    minimum_letters = min(list(counter_dict))
    
    if maximum_letters - minimum_letters == 1 and counter_dict[maximum_letters] == 1:
        return "YES"
    
    print(counter)
    print(counter_dict)
    return "NO"

############ Special String Again ############################################

def substrCount(n, s):
    total_count = 0
    i = 0
    while i < len(s):
        leftside_count, count = counter(s, i)
        total_count += count
        i += leftside_count
    return int(total_count)
    

def counter(s, i):
    char = s[i]
    leftside_count = 0
    rightside_count = 0
    change_sides = False
    j = i
    total_count = 0
    while j < len(s):
        if s[j] == char:
            if change_sides:
                rightside_count += 1
            else:
                leftside_count += 1
        else:
            if change_sides:
                break
            else:
                change_sides = True
        j += 1
    
    # We have already changed sides so eject
    total_count = (leftside_count + 1) * leftside_count / 2 + min(leftside_count, rightside_count)
    return leftside_count , total_count

############ Common Child #####################################################



##############################################################################
################### B O N U S ################################################

############ Creating a deep copy of an array ################################

def deepCopy(arr):
    default_arr = []
    for el in arr:
        if isinstance(el, list):
            default_arr.append(deepCopy(el))
        else:
            default_arr.append(el)
    return default_arr


############ Reverse an array with O(1) space complexity #####################

def reverse(arr):
    for i in range(len(arr)//2):
        arr[i], arr[~i] = arr[~i], arr[i]
    return arr
