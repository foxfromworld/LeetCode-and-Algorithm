# Source : https://leetcode.com/problems/reverse-words-in-a-string/
# Author : foxfromworld
# Date  : 12/03/2021
# First attempt 

class Solution:
  def reverseWords(self, s: str) -> str:
    return ' '.join(s.split()[::-1])
