# Source : https://leetcode.com/problems/rotate-string/
# Author : foxfromworld
# Date  : 03/11/2021
# Third attempt

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(goal) < len(s): return False
        return goal in s + s

# Date  : 03/11/2021
# Second attempt

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)-1, -1, -1):          
            if s[i:]  + s[0:i] == goal:
                return True
        return False
      
# Date  : 03/11/2021
# First attempt

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        s = list(s)
        for _ in range(len(s)-1):
            s.insert(0, s.pop())
            if ''.join(s) == goal:
                return True
        return False
