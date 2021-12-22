# time complexity O(n)
# space complexity O(n)

def makeAnagram(a, b):

    a_dict = {}
    deletion = 0

    for i in a:
        if i in a_dict:
            a_dict[i] += 1
        else:
            a_dict[i] = 1

    for j in b:
        if j in a_dict and a_dict[j] > 0:
            a_dict[j] -= 1
        else:
            deletion += 1

    for d in a_dict:
        if a_dict[d] > 0:
            deletion += a_dict[d]

    return deletion


print(makeAnagram("cde", "abc"))
