# Source : https://leetcode.com/problems/find-the-highest-altitude/
# Author : foxfromworld
# Date  : 13/11/2021
# First attempt

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt, ret = 0, 0
        for g in gain:
            alt = alt + g
            ret = max(alt, ret)
        return ret
