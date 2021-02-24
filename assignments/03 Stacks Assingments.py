from stacks import Stack_List as Stack

######### Reverse a String using Stack #######################################
######### Time Complexity: O(n) ##############################################
######### Space Complexity: O(n) #############################################

def reverse(s):
    reverser = Stack()
    new_string = ''
    for char in s:
        reverser.push(char)
    
    while not reverser.isEmpty():
        new_string += reverser.pop()

    return new_string

print(reverse("Joshua Maina"))

######### Valid Parentheses ##################################################
######### Time Complexity: O(n) ##############################################
######### Space Complexity: O(n) #############################################

openers_closers = {
    "(":")",
    "{":"}",
    "[":"]"
}
def isValid(s):
    stack = Stack()
    for char in s:
        if char in openers_closers:
            # Open brackets
            stack.push(char)
        else:
            if stack.isEmpty():
                return False
            open_bracket = stack.pop()
            if openers_closers[open_bracket] != char:
                return False
    if stack.isEmpty():
        return True
    return False

print(isValid("()"))
print(isValid("()[]{}({}[]{[]})"))

######### Simple Calculator ##################################################
######### Time Complexity: O(n) ##############################################
######### Space Complexity: O(n) #############################################
def evaluate(s):
    def update(sign, num_digit):
        if num_digit.strip() == '':
            return
        num = int(num_digit)
        stack.append(num if sign == "+" else -num)
    
    operators = {'+', '-', '(', ')'}
    num_digit = ''
    stack = []
    # At start point we start with positive
    sign = '+'
    i = 0
    while i < len(s):
        char = s[i]
        if char not in operators:
            num_digit += char
        elif char == "(":
            # Rerun the ops with a return value
            update(sign, num_digit)
            addition, sum_val = evaluate(s[i+1:])
            i += (addition + 1)
            update(sign, str(sum_val))
        elif char == ")":
            #Close the ops with the return value
            update(sign, num_digit)
            return i, sum(stack)
        else:
            update(sign, num_digit)
            sign = char
            num_digit = ''
        i += 1
    update(sign, num_digit)
    return sum(stack)

print(evaluate("1 + 2 + (2 + (2 + 4) + (1 + 3) )"))
