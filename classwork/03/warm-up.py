def evaluate(s):
    def update(sign, num):
        if sign == '+':
            stack.append(+num)
        else:
            stack.append(-num)
    operators = {'+', '-'}
    num_digit = ''
    stack = []
    # At start point we start with positive
    sign = '+'

    for i in range(len(s)):
        char = s[i]
        if char not in operators:
            num_digit += char
        else:
            update(sign, int(num_digit))
            sign = char
            num_digit = ''
    update(sign, int(num_digit))
    return sum(stack)

    

print(evaluate("1+1"))
print(evaluate("3 - 7"))
print(evaluate("4 + 8 - 2"))
print(evaluate("8 + 3 + 6 + 2 - 3"))
