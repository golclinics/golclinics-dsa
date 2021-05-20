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


if __name__ == "__main__":
    array_ = ['t', 'h', 'i', 's', ' ', 'i', 's', ' ', 'g', 'o', 'o', 'd']
    print(reverse_sentence(array_))
