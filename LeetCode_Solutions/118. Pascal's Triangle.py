# Source : https://leetcode.com/problems/pascals-triangle/
# Author : foxfromworld
# Date  : 15/10/2021
# First attempt

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1: return [[1]]
        elif numRows == 2: return [[1], [1, 1]]
        ret = [[1], [1, 1]]
        for i in range(2, numRows):
            temp = [1]
            for j in range(1, i):
                temp.append(ret[i-1][j-1] + ret[i-1][j])
            temp.append(1)
            ret.append(temp)
        return ret
            
