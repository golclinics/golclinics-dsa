#Write a method/function, reverse(A) that takes an array of integers, A and reverses it

def reverse(A):
    size = len(A)
    result = []
    for x in range(1, size + 1):
        result.append(A[-x]) #Used to append values starting from the last integer in the list
    return result

#Testing purposes
A = [3,2,1,0]
print(reverse(A))
