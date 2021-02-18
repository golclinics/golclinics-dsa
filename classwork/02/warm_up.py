from typing import List

def warmUp(nums: List[int], target: int) -> List[int]:
    numsDict = {}
    for index, item in enumerate(nums):
        diff = target - item
        if diff in numsDict:
            return numsDict[diff], index
        numsDict[item] = index
