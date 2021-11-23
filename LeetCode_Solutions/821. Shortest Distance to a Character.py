# Source : https://leetcode.com/problems/shortest-distance-to-a-character/
# Author : foxfromworld
# Date  : 23/11/2021
# First attempt 

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        target_idx = float('-inf')
        ret = []
        for i, ch in enumerate(s):
            if ch == c: target_idx = i
            ret.append(i - target_idx)
        target_idx = float('inf')
        for i in range(len(s)-1, -1, -1):
            if s[i] == c: target_idx = i
            ret[i] = min(ret[i], target_idx - i)
        return ret
