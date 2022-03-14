# Source : https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# Author : foxfromworld
# Date   : 14/03/2022
# First attempt

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 　5 7 7 8 8 8 8 8 10 
        # 　l       m        r
        # leftWise←|→ not leftWise
        def binarySearch(leftWise):
            l, r, i = 0, len(nums) - 1, -1
            while l <= r:
                m = (l + r) // 2     
                if nums[m] < target:
                    l = m + 1
                elif nums[m] > target:
                    r = m - 1
                else:
                    i = m
                    if leftWise:
                        r = m - 1
                    else:
                        l = m + 1
                  
            return i
        start = binarySearch(True)
        end = binarySearch(False)
        return [start, end]
