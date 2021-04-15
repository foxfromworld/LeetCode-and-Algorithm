# Source : https://leetcode.com/problems/add-digits/
# Author : foxfromworld
# Date  : 15/04/2021
# Third attempt

class Solution:
  def addDigits(self, num: int) -> int:
    if num == 0: return num
    return num%9 or 9 if num else 0

# Date  : 15/04/2021
# Second attempt
"""
*10 to the power of n -> 10pn
n = a0 x (10p0) + a1 x (10p1) + a2 x (10p2) + ... + an x (10pn)
=> n = a0 x ((9+1)p0) + a1 x ((9+1)p1) + a2 x ((9+1)p2) + ... + an x ((9+1)pn)
=> n = a0 x (9x0+1) + a1 x (9x1+1) + a2 x (9x11+1) + ... + an x ((9xn+1)
=> n = (a0x9x0+a0) + (a1x9x1+a1) + (a2x9x11+a2) + ... + (anx9xn+an)
=> n = (a0 + a1 + a2 + ... + an) +(a0x9x0 + a1x9x1+ a2x9x11 + ... + anx9xn)
=> n = (a0 + a1 + a2 + ... + an) +9(a1x1+ a2x11 + ... + anxn)
"""

class Solution:
  def addDigits(self, num: int) -> int:
    if num == 0: return num
    if num%9 == 0: return 9
    return num%9

# Date  : 15/04/2021
# First attempt

class Solution:
  def addDigits(self, num: int) -> int:
    if num < 10: return num
    while len(list(str(num))) > 1:
      num = sum([int(i) for i in list(str(num))])
    return num
