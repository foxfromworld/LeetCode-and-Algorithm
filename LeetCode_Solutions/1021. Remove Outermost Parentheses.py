# Source : https://leetcode.com/problems/remove-outermost-parentheses/
# Author : foxfromworld
# Date  : 16/02/2021
# First attempt 

class Solution:
  def removeOuterParentheses(self, S: str) -> str:
    returnStr = ""
    bracket = 0
    for i in range(len(S)):
      if S[i] =='(':
        bracket += 1
        if bracket >=2:
          returnStr += '('
      else:
        bracket -= 1
        if bracket != 0:
          returnStr += ')'
    return returnStr
