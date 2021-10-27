# Source : https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
# Author : foxfromworld
# Date  : 27/10/2021
# Third attempt

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        length = len(grid[0])
        ret = 0
        for row in grid:
            st, ed = 0, length
            while st < ed:
                mid = st + (ed - st) // 2
                if row[mid] < 0:
                    ed = mid
                else:
                    st = mid + 1
            ret += (length - st)
        return ret

# Date  : 27/10/2021
# Second attempt

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        ret = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] < 0:
                    ret += (col - c)
                    break
        return ret

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
