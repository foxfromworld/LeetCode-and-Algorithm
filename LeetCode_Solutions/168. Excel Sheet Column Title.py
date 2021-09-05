# Source : https://leetcode.com/problems/excel-sheet-column-title/
# Author : foxfromworld
# Date  : 05/09/2021
# Second attempt 
class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        title = ''
        while columnNumber > 0:
          quotient, remainder = divmod((columnNumber - 1), 26)
          title = alphabet[remainder] + title
          columnNumber = quotient
        return title

# Date  : 26/02/2021
# First attempt 

class Solution:
  def convertToTitle(self, n: int) -> str:
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    title = ''
    while n > 0:
      title = alphabet[(n - 1) % 26] + title
      n = (n - 1) // 26
    return title
