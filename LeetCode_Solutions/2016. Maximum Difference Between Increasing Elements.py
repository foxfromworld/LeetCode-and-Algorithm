# Source : https://leetcode.com/problems/maximum-difference-between-increasing-elements/
# Author : foxfromworld
# Date  : 27/09/2021
# First attempt

class Solution:
  def maximumDifference(self, nums: List[int]) -> int:
    current_min, ret = float('inf'), -1
    for j, val in enumerate(nums):
      if val > current_min:
        ret = max(ret, val - current_min)
      current_min = min(val, current_min)
    return ret
