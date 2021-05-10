# Source : https://leetcode.com/problems/sqrtx/
# Author : foxfromworld
# Date  : 10/05/2021
# Third attempt

# Date  : 10/05/2021
# Second attempt

class Solution:
  def mySqrt(self, x: int) -> int:
    if x <= 1: return x
    low, high = 2, x//2
    while low <= high:
      pivot = low + (high - low)//2
      pxp = pivot * pivot
      if pxp > x: high = pivot - 1
      elif pxp < x: low = pivot + 1 
      else: return pivot
    return high

# Date  : 08/05/2021
# First attempt

class Solution:
  def mySqrt(self, x: int) -> int:
    return int(math.sqrt(x))
