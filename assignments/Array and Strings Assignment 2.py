def reverse_array(array):
    middle = len(array) // 2
    for i in range(middle):
        array[i], array[~i] = array[~i], array[i]
    return array


def reverse_sentence(array_sentence):
    sentence = ""
    word = ""
    for char in array_sentence:
        if char == " ":
            sentence = " " + word + sentence
            word = ""
        else:
            word += char

    sentence = word + sentence
    return [char for char in sentence]


def minimum_swaps(arr):
    index = 0
    swaps = 0
    while index < len(arr):
        if (index + 1) != arr[index]:
            current = arr[index]
            arr[index], arr[current - 1] = arr[current - 1], arr[index]
            swaps += 1
        else:
            index += 1
    return swaps
