# Source : https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/
# Author : foxfromworld
# Date  : 13/12/2021
# First attempt

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort()
        for st, ed in ranges:
            if left < st:
                return False # if left is not in the range
            if left > ed: 
                continue # if the range is alreadt covering the larger end
            left = ed + 1
        return left > right
