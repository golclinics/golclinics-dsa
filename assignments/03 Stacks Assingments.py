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
    

        
