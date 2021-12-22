# assumes string has only braces
def is_balanced(s):

    opening_braces = {'(', '{', '['}
    stack = []

    braces = {')':'(', '}':'{', ']':'['}

    for char in s:
        if char in opening_braces:
            stack.append(char)
        elif braces[char]:
            brace = stack.pop()
            if brace != braces[char]:
                return False

    return len(stack) == 0


print(is_balanced("{[(])}"))
print(is_balanced("{[]}"))
