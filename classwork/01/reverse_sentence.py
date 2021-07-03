# Write a function reverseSentence(A) that takes in an array of characters, A, 
# and reverses the the "words" (not individual characters).

# Example:

# A = ['t', 'h', 'i', 's', ' ', 'i', 's', ' ', 'g', 'o', 'o', 'd'] 
# reverseSentence(A) A // ['g', 'o', 'o', 'd', ' ', 'i', 's', ' ', 't', 'h', 'i', 's']

def reverse_sentence(S):
    word = ""
    sentence = ""

    for char in S:
        if char == ' ':
            sentence = word + ' ' + sentence # reversed words
            word = "" # reset word on space encounter
        else:
            word += char

    if word != "":
        sentence = word + " " + sentence
    return sentence
# Time complexity O(n)
# Space complexity O(n)

print(reverse_sentence(['t', 'h', 'i', 's', ' ', 'i', 's', ' ', 'g', 'o', 'o', 'd']))

