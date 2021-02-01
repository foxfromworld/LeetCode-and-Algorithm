# Source : https://leetcode.com/problems/valid-parentheses/
# Author : foxfromworld
# Date  : 01/02/2021
# First attempt

class Solution:
  def isValid(self, s: str) -> bool:
    if not len(s)%2 == 0:
      return False
    parentheses = { ")":"(", "}":"{", "]":"[" }
    stack = []
    for p in s:
      if p in parentheses:
        left_parenthese = stack.pop() if stack else "X"
        if not left_parenthese == parentheses[p]:
          return False        
      else:
        stack.append(p)        
    return not stack #If the stack is empty (not stack), return True.
