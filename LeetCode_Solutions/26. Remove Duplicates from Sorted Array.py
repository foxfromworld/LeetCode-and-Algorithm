# Source : https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Author : foxfromworld
# Date  : 07/10/2021
# First attempt

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return
        curr = nums[0]
        pt = 1
        for i in range(1, len(nums)):
            if nums[i] > curr:
                nums[pt] = nums[i]
                pt += 1
                curr = nums[i]
        return pt
