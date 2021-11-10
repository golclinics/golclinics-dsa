# Function to reverse array

def reverse(A):
    A = A[::-1]
    return A


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    print(reverse(a))
