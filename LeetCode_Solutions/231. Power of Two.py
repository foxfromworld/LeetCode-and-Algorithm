# Source : https://leetcode.com/problems/power-of-two/
# Author : foxfromworld
# Date  : 27/11/2021
# First attempt

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return not (n & (n-1)) if n > 0 else 0
