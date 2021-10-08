# Source : https://leetcode.com/problems/search-insert-position/
# Author : foxfromworld
# Date  : 08/10/2021
# Second attempt 

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                right -= 1
            else:
                left += 1
        return left

# Date  : 08/10/2021
# First attempt 

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                right -= 1
            else:
                left += 1
        return left
