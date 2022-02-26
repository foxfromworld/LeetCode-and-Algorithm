# Source : https://leetcode.com/problems/zigzag-conversion/
# Author : foxfromworld
# Date  : 26/02/2022
# First attempt

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        """
        S = "ABCDEFGH"
        numRows = 3
                                  
        step = 1   A  E        row = 0
               1   B D F H           1
               -1  C    G            2
        """
        row, step = 0, 1
        ret = [""] * numRows
        for ch in s:
            ret[row] += ch
            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1
            row += step
        return "".join(ret)
