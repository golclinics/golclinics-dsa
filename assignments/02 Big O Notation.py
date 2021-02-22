########## Flatland Space Station ##############################################
########## Time Complexity : O(nlog(n)) ########################################
########## Space Complexity : O(n) #############################################

def flatlandSpaceStations(n, c):
    sorted_spacestations = sorted(c)
    max_distance = 0
    previous_station = sorted_spacestations[0]
    for i in range(1, len(sorted_spacestations)):
        local_max_distance = (sorted_spacestations[i] - previous_station) // 2 
        max_distance = max(max_distance, local_max_distance)
        previous_station = sorted_spacestations[i]

    max_distance = max(max_distance, sorted_spacestations[0]-0, n - 1 - sorted_spacestations[len(c) - 1])
    return max_distance

########## Between Two Sets ####################################################
########## Time Complexity : Not really sure ###################################
########## Space Complexity : O(1) #############################################

from math import gcd
def getTotalX(a, b):
    # Write your code here
    lcm = 1
    count = 0

    for value in a:
        lcm = lcm * value // gcd(lcm, value)

    for value in range(lcm, max(b) + lcm, lcm):
        if check(value, b):
            count += 1
            print(value)
    return count
            

def check(lcm, b):
    for value in b:
        if value % lcm != 0:
            return False
    return True

########## Non-Divisible Subset ################################################
########## Time Complexity : O(n) ##############################################
########## Space Complexity : O(n) #############################################
def nonDivisibleSubset(k, s):
    # Write your code here
    counter_dict = dict()
    for num in s:
        remainder = num % k
        if remainder in counter_dict:
            counter_dict[remainder] += 1
        else:
            counter_dict[remainder] = 1
    total_ = 0
    for i in range(k//2 + 1):
        if i == 0 or (i*2) == k:
            total_ += min(counter_dict.get(i, 0), 1)
        else:
            total_ += max(counter_dict.get(i, 0), counter_dict.get(k-i, 0))
    return total_

########## Bigger is Greater ###################################################
########## Time Complexity : O(n) ##############################################
########## Space Complexity : O(n) #############################################


# Complete the biggerIsGreater function below.
def biggerIsGreater(w):
    word_length = len(w)
    previous_char = w[-1]
    previous_index = word_length - 1
    for i in range(word_length - 2, -1, -1):
        current_char = w[i]
        if ord(previous_char) > ord(current_char):
            # In this case a change is possible
            previous_index -= 1
            previous_char = current_char
            break
        previous_index -= 1
        previous_char = current_char
    else:
        return "no answer"

    substring = sorted_alphabet(w[previous_index:])
    smallest_char_index = None
    for i in range(len(substring)):
        letter = substring[i]
        if letter > previous_char:
            smallest_char_index = i
            break
    return w[:previous_index] + substring[smallest_char_index] + substring[:smallest_char_index] + substring[smallest_char_index+1:]

def sorted_alphabet(w):
    # Faster algo for sorting the word O(n)
    arr = [0 for _ in range(26)]
    sorted_w = ''
    for letter in w:
        arr[ord(letter) - ord('a')] += 1
    for i in range(len(arr)):
        num = arr[i]
        sorted_w += (chr(ord('a') + i) * num)
    return sorted_w


