# Source : https://leetcode.com/problems/check-if-n-and-its-double-exist/
# Author : foxfromworld
# Date  : 10/11/2021
# First attempt

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for i in arr:
            if i%2 == 0 and i/2 in seen:
                return True
            if i*2 in seen:
                return True
            seen.add(i)
        return False
