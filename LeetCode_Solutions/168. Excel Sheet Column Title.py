# Source : https://leetcode.com/problems/excel-sheet-column-title/
# Author : foxfromworld
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
