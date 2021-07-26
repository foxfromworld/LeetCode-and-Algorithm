# Source : https://leetcode.com/problems/student-attendance-record-i/
# Author : foxfromworld
# Date  : 26/07/2021
# Third attempt

class Solution(object):
  def checkRecord(self, s):
    """
    :type s: str
    :rtype: bool
    """
    for i in range(len(s)-2):
      if s[i:i+3] == 'LLL':
        return False
    return s.count('A') <= 1

# Date  : 26/07/2021
# Second attempt

class Solution(object):
  def checkRecord(self, s):
    """
    :type s: str
    :rtype: bool
    """
    return s.count('A') <=1 and s.count('LLL') < 1

# Date  : 26/07/2021
# First attempt

class Solution(object):
  def checkRecord(self, s):
    """
    :type s: str
    :rtype: bool
    """
    countA = 0
    s = list(s)
    for i, ch in enumerate(s):
      print(i, ch)
      if ch == 'A':
        countA += 1
        if countA >=2:
          return False
      if ch == 'L' and i > 0 and i < len(s)-1:
        if s[i-1] == 'L' and s[i+1] == 'L':
          return False
    return True
