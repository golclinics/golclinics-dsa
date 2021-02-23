import re


def evaluate(S):
    # Remove all whitespaces in string
    s = S.replace(' ', '')

    # Split string at operators  into array
    arr = re.split(r'(\D)', s)

    # Intialize first element of array as result
    result = int(arr[0])

    # Iterate through the array operating on the numbers depending on operator
    # and update result
    for i in range(0, len(arr) - 2, 2):

        if arr[i + 1] == '+':
            result += int(arr[i + 2])

        else:
            result -= int(arr[i + 2])

    return result


if __name__ == '__main__':
    s = "8 + 3 + 6 + 2 - 3"

    print(evaluate(s))
