# Source : https://leetcode.com/problems/largest-number-at-least-twice-of-others/
# Author : foxfromworld
# Date  : 25/11/2021
# First attempt

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        nums_ = sorted(nums)
        for num in nums_[:-1]:
            if num * 2 > nums_[-1]:
                return -1            
        return nums.index(nums_[-1])
