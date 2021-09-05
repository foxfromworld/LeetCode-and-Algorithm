# Source : https://leetcode.com/problems/length-of-last-word/
# Author : foxfromworld
# Date  : 05/09/2021
# Second attempt 

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split(' ')
        while words[-1] == '':
          words.pop()
        return len(words[-1])

# Date  : 19/02/2021
# First attempt 

class Solution:
  def lengthOfLastWord(self, s: str) -> int:
    words = s.split(' ')
    while words[-1] == '' and len(words)>1 :
      words.pop()
    return len(words[-1])
