# Source : https://leetcode.com/problems/valid-sudoku/
# Author : foxfromworld
# Date   : 19/03/2022
# First attempt

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_row = [set() for _ in range(9)]
        seen_col = [set() for _ in range(9)]
        seen_grid = [set() for _ in range(9)]
        for row in range(9):
            for col in range(9):
                curr = board[row][col]
                if curr == '.':
                    continue
                grid = (3 * (row // 3) + col //3)
                if curr in seen_row[row]:
                    return False
                if curr in seen_col[col]:
                    return False
                if curr in seen_grid[grid]:
                    return False
                
                seen_row[row].add(curr)
                seen_col[col].add(curr)
                seen_grid[grid].add(curr)
        return True
