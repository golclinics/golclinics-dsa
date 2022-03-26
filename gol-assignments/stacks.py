def reverse_string(string):
    stack = []
    for chr in string:
        stack.append(chr)

    new_string = ""
    while len(stack):
        new_string += stack.pop()

    return new_string


def brackets_match(string_of_brackets):
    close_to_open = {
        '}': '{',
        ')': '(',
        '[': ']'
    }
    stack = []
    for bracket in string_of_brackets:
        if bracket in close_to_open:
            if len(stack):
                opener = stack.pop()
                if opener != close_to_open[bracket]:
                    return False
            else:
                return False
        else:
            stack.append(bracket)
    return not len(stack)