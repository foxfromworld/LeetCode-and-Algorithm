# Source : https://leetcode.com/problems/reformat-the-string/
# Author : foxfromworld
# Date  : 25/03/2021
# Third attempt

class Solution:
  def reformat(self, s: str) -> str:
    s_l, s_d = [], []
    for ch in s:
      if "a" <= ch <= "z":
        s_l.append(ch)
      else:
        s_d.append(ch)
    lenDiff = len(s_l) - len(s_d)
    result = ""
    if abs(lenDiff) > 1: return ""
    if lenDiff < 0:
      s_l, s_d = s_d, s_l
    for i in range(len(s_d)):
      result += s_l[i]
      result += s_d[i]
    if  lenDiff != 0: 
      result += s_l[-1]
    return result

# Date  : 25/03/2021
# Second attempt

class Solution:
  def reformat(self, s: str) -> str:
    s_l, s_d = [], []
    for ch in s:
      if "a" <= ch <= "z":
        s_l.append(ch)
      else:
        s_d.append(ch)
    lenDiff = len(s_l) - len(s_d)
    result = ""
    if abs(lenDiff) > 1: return ""
    elif lenDiff >= 0:
      for i in range(len(s_d)):
        result += s_l[i]
        result += s_d[i]
      if  lenDiff != 0: 
        result += s_l[-1]
      return result        
    else:
      for i in range(len(s_l)):
        result += s_d[i]
        result += s_l[i]
      result += s_d[-1]        
      return result

# Date  : 25/03/2021
# First attempt

class Solution:
  def reformat(self, s: str) -> str:
    letters = "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"

    s_l, s_d = [], []
    for ch in s:
      if ch in letters:
        s_l.append(ch)
      else:
        s_d.append(ch)
    lenDiff = len(s_l) - len(s_d)
    result = ""
    if abs(lenDiff) > 1: return ""
    elif lenDiff >= 0:
      for i in range(len(s_d)):
        result += s_l[i]
        result += s_d[i]
      if  lenDiff != 0: 
        result += s_l[-1]
      return result        
    else:
      for i in range(len(s_l)):
        result += s_d[i]
        result += s_l[i]
      result += s_d[-1]        
      return result
