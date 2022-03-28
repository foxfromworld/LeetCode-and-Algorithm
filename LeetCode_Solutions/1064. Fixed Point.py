# Source : https://leetcode.com/problems/fixed-point/
# Author : foxfromworld
# Date   : 28/03/2022
# First attempt

class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        lo, hi = 0, len(arr) - 1
        ret = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if arr[mid] == mid:
                ret = mid
                hi = mid - 1
            elif arr[mid] < mid:
                lo = mid + 1   
            else: # arr[mid] > mid
                hi = mid - 1
        return ret
