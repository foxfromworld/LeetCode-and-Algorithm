# Source : https://leetcode.com/problems/set-matrix-zeroes/
# Author : foxfromworld
# Date  : 20/10/2021
# First attempt

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, col = set(), set()
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                if matrix[y][x] == 0:
                    row.add(y)
                    col.add(x)
        for r in row:
            matrix[r][:] = [0] * len(matrix[0])
        for c in col:
            for i in range(len(matrix)):
                matrix[i][c] = 0
