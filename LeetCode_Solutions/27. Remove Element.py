# Source : https://leetcode.com/problems/remove-element/
# Author : foxfromworld
# Date  : 07/10/2021
# First attempt

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pt = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[pt] = nums[i]
                pt += 1
        return pt
