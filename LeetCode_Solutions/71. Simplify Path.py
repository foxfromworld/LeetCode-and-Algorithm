# Source : https://leetcode.com/problems/simplify-path/
# Author : foxfromworld
# Date  : 22/10/2021
# First attempt

class Solution:
    def simplifyPath(self, path: str) -> str:
        ret = []
        for dir in path.split('/'):
            if dir == '.':
                continue
            elif dir == '..':
                if ret:
                    ret.pop()
            elif dir:
                ret.append(dir)
        return '/' + '/'.join(ret)
