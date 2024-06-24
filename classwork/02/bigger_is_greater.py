def biggerIsGreater(w):
    w = list(w)
    x = len(w)-1
    while x > 0 and w[x-1] >= w[x]:
        x -= 1

    if x <= 0:
        return 'no answer'

    j = len(w) - 1
    while w[j] <= w[x - 1]:
        j -= 1
    
    w[x-1], w[j] = w[j], w[x-1]

    w[x:] = w[len(w)-1:x-1:-1]

    return ''.join(w)