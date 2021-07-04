def isValid(self, s):
    """
        :type s: str
        :rtype: bool
        """
    # if len of the string is not even, not valid
    # if len(s)%2 != 0:
    #     return False

    stack = []
    params = {"}": "{", ")": "(", "]": "["}

    for char in s:
        # check if closing param
        if char in params:

            top = stack.pop() if stack else '0'

            if params.get(char) != top:
                return False
        else:
            # opening param append on stack
            stack.append(char)

    return not stack
