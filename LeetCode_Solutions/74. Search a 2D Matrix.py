# Source : https://leetcode.com/problems/search-a-2d-matrix/
# Author : foxfromworld
# Date  : 17/10/2021
# Second attempt

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = len(matrix), len(matrix[0])
        left, right = 0, (r * c) -1
        
        while left <= right:
            pivot_idx = (left + right) // 2         
            row, col = pivot_idx // c, pivot_idx % c
            val = matrix[row][col]
            if  val == target:
                return True
            elif val < target:
                left = pivot_idx + 1
            else:
                right = pivot_idx - 1 
        return False
            

# Date  : 17/10/2021
# First attempt

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if target == row[0] or target == row[-1]:
                return True
            elif row[0] <= target <= row[-1]:
                print(target, row)
                return True if target in row else False
        return False
