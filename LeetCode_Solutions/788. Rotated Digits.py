# Source : https://leetcode.com/problems/rotated-digits/
# Author : foxfromworld
# Date  : 06/04/2021
# First attempt 

class Solution:
  def rotatedDigits(self, N: int) -> int:
    ans = 0
    for i in range(1, N+1):
      digit = str(i)
      if any([ch in '2569' for ch in digit]) and all([ch not in '347' for ch in digit]):
        ans += 1
    return ans
