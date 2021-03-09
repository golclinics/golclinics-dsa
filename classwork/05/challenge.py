def wordFrequency(S):

    d = {}

    arr = S.split()

    for i in arr:

        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    max_val = 0
    c = ''

    for i in d:
        if d[i] > max_val:
            c = i
            max_val = d[i]
    print(c)
    print(max_val)    
