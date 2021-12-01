# Source : https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/
# Author : foxfromworld
# Date  : 01/12/2021
# First attempt

class Solution:
    def average(self, salary: List[int]) -> float:
        mx, mn = float('-inf'), float('inf')
        result = 0
        for sa in salary:
            result += sa
            if sa > mx:
                mx = sa
            if sa < mn:
                mn = sa
        return (result - mx - mn) / (len(salary) - 2)
