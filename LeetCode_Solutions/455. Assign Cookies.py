# Source : https://leetcode.com/problems/assign-cookies/
# Author : foxfromworld
# Date  : 22/11/2021
# Second attempt

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse = True)
        s.sort(reverse = True)
        idx = 0
        for kid in g:
            if idx < len(s) and s[idx] >= kid:
                idx += 1
        return idx
      
# Date  : 22/11/2021
# First attempt

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse = True)
        s.sort(reverse = True)
        idx = 0
        for i in range(len(g)):
            if idx < len(s) and s[idx] >= g[i]:
                idx += 1
        return idx
