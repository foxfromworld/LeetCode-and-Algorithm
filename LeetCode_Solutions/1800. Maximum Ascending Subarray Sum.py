# Source : https://leetcode.com/problems/maximum-ascending-subarray-sum/
# Author : foxfromworld
# Date  : 24/10/2021
# Second attempt 

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ret, temp = 0, 0
        for i in range(len(nums)):
            if nums[i] <= nums[i-1]:
                temp = 0
            temp += nums[i]
            ret = max(temp, ret)
        return ret

# Date  : 24/10/2021
# First attempt 

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ret, st, ed = 0, 0, 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]: 
                ed = i
            else:
                ret = max(ret, sum(nums[st : ed+1]))
                st, ed = i, i
        ret = max(ret, sum(nums[st:]))
        return ret
