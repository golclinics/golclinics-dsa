def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    l = r = 0
    n = len(nums)

    while n > 0:

        if nums[r] == val:
            r += 1
        else:
            nums[l] = nums[r]
            r += 1
            l += 1
        n -= 1
    return l

print(removeElement([3,2,2,3], 2))