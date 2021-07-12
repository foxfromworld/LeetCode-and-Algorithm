# Source : https://leetcode.com/problems/base-7/
# Author : foxfromworld
# Date  : 12/07/2021
# Third attempt

class Solution(object):
  def convertToBase7(self, num):
    """
    :type num: int
    :rtype: str
    """
    num1, ret = abs(num), ""
    while num1: 
      ret = str(num1 % 7) + ret
      num1 //= 7
    return '-' * (num < 0) + ret or "0"

# Date  : 12/07/2021
# Second attempt
  
class Solution(object):
  def convertToBase7(self, num):
    """
    :type num: int
    :rtype: str
    """
    if num == 0: return "0"
    num1, ret = abs(num), ""
    while num1: 
      ret = str(num1 % 7) + ret
      num1 //= 7
    return ret if num > 0 else "-" + ret
  
# Date  : 12/07/2021
# First attempt
  
  class Solution(object):
  def convertToBase7(self, num):
    """
    :type num: int
    :rtype: str
    """
    if -7 < num < 7: return str(num)
    num1 = abs(num)
    ret = ""
    while num1 >= 7: 
      ret = str(num1 % 7) + ret
      num1 //= 7
    ret = str(num1) + ret
    return ret if num > 0 else "-" + ret
