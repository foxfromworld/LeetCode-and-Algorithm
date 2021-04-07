# Source : https://leetcode.com/problems/rotated-digits/
# Author : foxfromworld
# Date  : 07/04/2021
# Fourth attempt 

class Solution(object):
  def rotatedDigits(self, N: int) -> int:
    set1 = set([0, 1, 2, 5, 6, 8, 9]) # 7**
    set2 = set([0, 1, 8]) # 3**
    col = set()
    ans = 0
    N = [int(ch) for ch in str(N)]
    for i, digit in enumerate(N):
      for j in range(digit):
        if j in set1:
          ans += 7**(len(N) - i - 1)
        if col.issubset(set2) and j in set2:
          ans -= 3**(len(N) - i - 1)
      if digit not in set1:
        return ans
      col.add(digit)
    return ans + (col.issubset(set1) and not col.issubset(set2))

# Date  : 06/04/2021
# Third attempt 

class Solution:
  def rotatedDigits(self, N: int) -> int:
    ans = 0
    for i in range(1, N+1):
      digit = str(i)
      ans += any([ch in '2569' for ch in digit]) and not any([ch in '347' for ch in digit])
    return ans

# Date  : 06/04/2021
# Second attempt 

class Solution:
  def rotatedDigits(self, N: int) -> int:
    ans = 0
    for i in range(1, N+1):
      digit = str(i)
      ans += any([ch in '2569' for ch in digit]) and all([ch not in '347' for ch in digit])
    return ans

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
