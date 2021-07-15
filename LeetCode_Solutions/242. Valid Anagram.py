# Source : https://leetcode.com/problems/valid-anagram/
# Author : foxfromworld
# Date  : 15/07/2021
# Second attempt

class Solution(object):
  def isAnagram(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    ""
    return all([s.count(c) == t.count(c) for c in "abcdefghijklmnopqrstuvwxyz"])

# Date  : 15/07/2021
# First attempt

class Solution(object):
  def isAnagram(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    ""
    for c in "abcdefghijklmnopqrstuvwxyz":
      if s.count(c) != t.count(c):
        return False
    return True
