# Source : https://leetcode.com/problems/longest-continuous-increasing-subsequence/
# Author : foxfromworld
# Date  : 07/12/2021
# First attempt

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        start, ret = 0, 0
        for i, num in enumerate(nums):
            if i > 0 and nums[i-1] >= num:
                start = i
            ret = max(ret, i - start + 1)
        return ret
