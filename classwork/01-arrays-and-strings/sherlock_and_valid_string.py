def isValid(s):
    char_dict = {}
    for char in s:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    minimum_count = char_dict[char]
    maximum_count = char_dict[char]

    count_dict = {}
    for char, value in char_dict.items():
        if value in count_dict:
            count_dict[value] += 1
        else:
            count_dict[value] = 1
        if value < minimum_count:
            minimum_count = value
        if value > maximum_count:
            maximum_count = value

    if len(count_dict) == 1:
        return 'YES'
    elif len(count_dict) == 2:
        if count_dict[maximum_count] == 1 and maximum_count - minimum_count == 1:
            return 'YES'
        elif count_dict[minimum_count] == 1 and minimum_count == 1:
            return 'YES'
    return 'NO'

