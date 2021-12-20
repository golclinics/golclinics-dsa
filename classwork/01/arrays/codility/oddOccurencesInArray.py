def solution(A):
    if len(A) < 1:
        return A
    
    count_dict = {}
    for val in A:
        if val in count_dict:
            count_dict[val] += 1
        else:
            count_dict[val] = 1

    for val in count_dict:
        if count_dict[val] % 2 != 0:
            return val
