# Source : https://leetcode.com/problems/strobogrammatic-number/
# Author : foxfromworld
# Date  : 04/05/2021
# Second attempt

class Solution:
  def isStrobogrammatic(self, num: str) -> bool:
    dict = {'1':'1', '6':'9', '8':'8', '9':'6', '8':'8', '0':'0'}
    left = 0
    right = len(num) - 1
    while right >= left:
      if num[left] not in dict or dict[num[left]] != num[right]:
        return False
      left += 1
      right -= 1
    return True
  
# Date  : 04/05/2021
# First attempt

class Solution:
  def isStrobogrammatic(self, num: str) -> bool:
    dict = {'1':'1', '6':'9', '8':'8', '9':'6', '8':'8', '0':'0'}
    newStr = ''
    for ch in num:
      if ch in dict:
        newStr = dict[ch] + newStr
      else:
        return False
    return True if newStr == num else False
