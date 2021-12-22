def evaluate(S):
    s =  S.split(" ") # remove spaces
    stack = []
    n = len(s) - 1
    i = 0

    while n >= 0:

        if s[i] == '+':
            i += 1
            stack.append(int(s[i]))
            i += 1
            n -= 2
        elif s[i] == '-':
            i += 1
            stack.append(-int(s[i]))
            i += 1
            n -= 2
        else:
            stack.append(int(s[i]))
            i += 1
            n -= 1


    
    return sum(stack)

# driver code
print(evaluate('3 + 5 - 2 - 2'))