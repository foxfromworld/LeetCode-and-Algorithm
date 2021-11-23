# Source : https://leetcode.com/problems/find-pivot-index/
# Author : foxfromworld
# Date  : 23/11/2021
# First attempt

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        SUM = sum(nums)
        leftSUM = 0
        for i, num in enumerate(nums):
            if leftSUM == SUM - leftSUM - num:
                return i
            leftSUM += num
        return -1
