# Source : https://leetcode.com/problems/find-the-distance-value-between-two-arrays/
# Author : foxfromworld
# Date  : 05/01/2021
# First attempt

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        def notBtw(e):
            high = len(arr2)
            low = 0
            while low < high:
                mid = (high + low) // 2
                if abs(e - arr2[mid]) <= d:
                    return False
                elif e - arr2[mid] < 0: # To narrow the range
                    high = mid
                else:
                    low = mid + 1
            return True
        return sum([notBtw(e) for e in arr1])
