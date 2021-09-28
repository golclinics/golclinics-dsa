def wordFrequency(S):
    arr_words = S.split()
    if len(arr_words) == 0:
        return 0
    Counter = dict()
    for word in arr_words:
        if word in Counter:
            Counter[word] += 1
        else:
            Counter[word] = 1
    return max(Counter.values())

print(wordFrequency("Life is so so good"))
print(wordFrequency("All coders are introverts, George is a coder, therefore George is an introvert"))
print(wordFrequency("Life is good"))
print(wordFrequency(""))
