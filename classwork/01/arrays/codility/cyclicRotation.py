# Time -> O(n), Space -> O(1)
def cyclicRotate(arr, k):
    # Base Case -> arr has 1 item or less or K is 0
    if len(arr) <= 1 or k <= 0:
        return arr
    
    #In-place rotation
    for i in range(k):
        temp = arr.pop()
        arr.insert(0, temp)

    return arr
