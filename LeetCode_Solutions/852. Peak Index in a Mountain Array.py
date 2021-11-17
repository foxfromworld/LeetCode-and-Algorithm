# Source : https://leetcode.com/problems/peak-index-in-a-mountain-array/
# Author : foxfromworld
# Date  : 17/11/2021
# First attempt

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        idx, peak = 0, 0
        for i, m in enumerate(arr):
            if m > peak:
                peak = m
                idx = i
        return idx
