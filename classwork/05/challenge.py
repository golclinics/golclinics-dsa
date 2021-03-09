def wordFrequency(S):

    d = {}

    arr = S.split()
    max_val = 0
    c = ''

    for i in arr:

        if i in d:
            d[i] += 1

            if d[i] > max_val:
                c = i
                max_val = d[i]
        else:
            d[i] = 1

    print(c)
    print(max_val)    

# Time and space complexity O(N)
# plot a histogram for each occurence of words

wordFrequency("hello there hello there there")
    