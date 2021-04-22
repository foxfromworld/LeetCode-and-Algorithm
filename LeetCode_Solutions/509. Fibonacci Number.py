# Source : https://leetcode.com/problems/fibonacci-number/
# Author : foxfromworld
# Date  : 22/04/2021
# Second attempt 

class Solution:
  def fib(self, N: int) -> int:
    if N <= 1: return N
    last = 1
    bflast = 0
    for i in range(2, N+1):
      current = bflast + last
      bflast = last      
      last = current
    return current

# Date  : 22/04/2021
# First attempt 

class Solution:
  def fib(self, N: int) -> int:
    if N == 0 or N ==1: return N
    fibL = [0, 1]
    while len(fibL) < N+1:
      fibL.append(fibL[-1] + fibL[-2])
    return fibL[-1]
