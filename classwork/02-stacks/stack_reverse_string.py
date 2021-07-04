def reverse_string_stack(S):
    stack = []
    str = ""

    for i in S:
        stack.append(i)
    
    while len(stack) > 0:
        str = str + stack.pop()
    
    return str

print(reverse_string_stack("hello"))