# Source : https://leetcode.com/problems/integer-break/
# Author : foxfromworld
# Date  : 13/02/2022
# First attempt

class Solution:
    def integerBreak(self, n: int) -> int:
        ret = 1
        if n <= 3:
            return n -1
        while 4 < n or n > 10:
            ret *= 3
            n -= 3
        return ret * n
