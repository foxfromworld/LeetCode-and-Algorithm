# Source : https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
# Author : foxfromworld
# Date  : 27/10/2021
# First attempt

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        col, row = len(grid[0]), len(grid)
        ret = 0
        for r in range(row-1, -1 , -1):
            for c in range(col-1, -1 , -1):
                if grid[r][c] >= 0:
                    break
                else:
                    ret += 1
        return ret
