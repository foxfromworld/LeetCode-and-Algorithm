# Source : https://leetcode.com/problems/container-with-most-water/
# Author : foxfromworld
# Date  : 01/03/2022
# First attempt

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        ret = 0
        while left < right:
            ret = max((right - left)*min(height[left], height[right]), ret) 
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ret
