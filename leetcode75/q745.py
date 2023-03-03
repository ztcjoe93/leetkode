from typing import List

# https://leetcode.com/problems/find-pivot-index/

def pivotIndex(nums: List[int]) -> int:
    arr = [0]
    cum_sum = 0
    # get total sum, and form an array of cumulative sum
    for i in range(len(nums)):
        cum_sum += nums[i]
        arr.append(cum_sum)
    
    for i in range(len(nums)):
        if (cum_sum - nums[i])/2 == arr[i]:
            return i
    
    return -1
