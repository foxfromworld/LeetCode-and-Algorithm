# Source : https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/
# Author : foxfromworld
# Date  : 03/08/2021
# First attempt

#  0  1   2  3  -
#  - -4  -3 -2 -1
# 20 75  81 82 95
#        ▔▔▔▔   # nums[-4] - nums[0]　　　
# ▔       ▔▔▔   # nums[-3] - nums[1]
# ▔▔▔       ▔   # nums[-2] - nums[2]
# ▔▔▔▔          # nums[-1] - nums[3]

class Solution(object):
  def minDifference(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) <= 4: return 0
    nums.sort()
    return min(
          nums[-4] - nums[0],
          nums[-3] - nums[1],
          nums[-2] - nums[2],
          nums[-1] - nums[3])
