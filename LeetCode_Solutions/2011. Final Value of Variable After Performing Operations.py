# Source : https://leetcode.com/problems/final-value-of-variable-after-performing-operations/
# Author : foxfromworld
# Date  : 27/09/2021
# Third attempt

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ret = 0
        for op in operations:
            if op in ('X++', '++X'):
                ret += 1
            else:
                ret -= 1
        return ret

# Date  : 27/09/2021
# Second attempt

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ret = 0
        for op in operations:
            if op == 'X++' or op == '++X':
                ret += 1
            else:
                ret -= 1
        return ret

# Date  : 27/09/2021
# First attempt

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ret = 0
        for op in operations:
            if op[0] == '+' or op[-1] == '+':
                ret += 1
            else:
                ret -= 1
        return ret
