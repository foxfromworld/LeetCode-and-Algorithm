# Source : https://leetcode.com/problems/transpose-matrix/
# Author : foxfromworld
# Date  : 13/11/2021
# Fourth attempt

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ret = []
        for c in range(len(matrix[0])):
            temp = []
            for r in range(len(matrix)):
                temp.append(matrix[r][c])
            ret.append(temp)
        return ret

# Date  : 13/11/2021
# Third attempt

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ret = [[] for _ in range(len(matrix[0]))]
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                ret[c].append(val)
        return ret

# Date  : 13/11/2021
# Second attempt

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ret = [[0] * len(matrix) for _ in range(len(matrix[0]))]
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                ret[c][r] = val
        return ret

# Date  : 13/11/2021
# First attempt

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return zip(*matrix)
