# Source : https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
# Author : foxfromworld
# Date  : 04/08/2021
# First attempt

class Solution(object):
  def maxScore(self, cardPoints, k):
    """
    :type cardPoints: List[int]
    :type k: int
    :rtype: int
    """
    if len(cardPoints) == k:
      return sum(cardPoints)
    curr = sum(cardPoints[0:k])
    prev = curr
    for i in range(1, k + 1):
      prev += cardPoints[-i] - cardPoints[k - i]
      curr = max(curr, prev)
    return curr
