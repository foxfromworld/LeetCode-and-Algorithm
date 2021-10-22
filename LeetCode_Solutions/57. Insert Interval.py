# Source : https://leetcode.com/problems/insert-interval/
# Author : foxfromworld
# Date  : 22/10/2021
# First attempt

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        ret = []
        for intv in intervals:
            if not ret or ret[-1][1] < intv[0]:
                ret.append(intv)
            else:
                ret[-1][1] = max(intv[1], ret[-1][1])
        return ret
            
