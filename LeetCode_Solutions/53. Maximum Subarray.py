# Source : https://leetcode.com/problems/maximum-subarray/
# Author : foxfromworld
# Date  : 19/03/2022
# Second attempt 

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ret, curr = float('-inf'), 0
        for _, val in enumerate(nums):           
            curr += val
            ret = max(curr, ret)
            if curr < 0:
                curr = 0
        return ret

# Date  : 09/10/2021
# First attempt 

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)
