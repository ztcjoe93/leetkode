from typing import List

# https://leetcode.com/problems/running-sum-of-1d-array

def runningSum(nums: List[int]) -> List[int]:
    arr = []
    cum_sum = 0
    for i in nums:
        cum_sum += i
        arr.append(cum_sum)
    
    return arr
