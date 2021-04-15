# Source : https://leetcode.com/problems/add-digits/
# Author : foxfromworld
# Date  : 15/04/2021
# First attempt

class Solution:
  def addDigits(self, num: int) -> int:
    if num < 10: return num
    while len(list(str(num))) > 1:
      num = sum([int(i) for i in list(str(num))])
    return num
