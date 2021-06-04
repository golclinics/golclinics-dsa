# Write a function reverseSentence(A) that takes in an array of characters, A, 
# and reverses the the "words" (not individual characters).

# Example:

# A = ['t', 'h', 'i', 's', ' ', 'i', 's', ' ', 'g', 'o', 'o', 'd'] 
# reverseSentence(A) A // ['g', 'o', 'o', 'd', ' ', 'i', 's', ' ', 't', 'h', 'i', 's']

def get_words(S):
    sentence = []
    words = []

    for s in S:
        if s != ' ':
            words.append(s)
        else:
            sentence.append(words)
            words = []

    sentence.append(words)

    return sentence

def reverse_sentence(S):

    words = get_words(S)
    res = []

    for i in range(len(words) - 1, -1, -1):
        for c in words[i]:
            res.append(c)
        res.append(' ')
    
    return res[:-1]


print(reverse_sentence(['t', 'h', 'i', 's', ' ', 'i', 's', ' ', 'g', 'o', 'o', 'd']))
