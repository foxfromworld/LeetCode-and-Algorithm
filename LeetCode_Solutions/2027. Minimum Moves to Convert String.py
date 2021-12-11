# Source : https://leetcode.com/problems/minimum-moves-to-convert-string/
# Author : foxfromworld
# Date  : 10/12/2021
# First attempt

class Solution:
    def minimumMoves(self, s: str) -> int:
        index = 0
        ret = 0
        while index < len(s):
            if s[index] == 'X':
                ret += 1
                index += 3
            else:
                index += 1
        return ret
