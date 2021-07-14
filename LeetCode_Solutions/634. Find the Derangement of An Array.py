# Source : https://leetcode.com/problems/find-the-derangement-of-an-array/
# Author : foxfromworld
# Date  : 14/07/2021
# First attempt

class Solution(object):
  def findDerangement(self, n):
    """
    :type n: int
    :rtype: int
    """
    # !n=(n-1)(!(n-1)+!(n-2))
    #       X + Y
    modulo = 10**9 + 7
    X = 1 # i = 0
    Y = 0 # i = 1
    for i in range(2, n + 1):
      X, Y = Y, (i - 1) * (X + Y) % modulo
    return Y
