# Source : https://leetcode.com/problems/contains-duplicate-ii/
# Author : foxfromworld
# Date  : 12/03/2021
# First attempt 

class Solution:
  def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    dict_ = {}
    for i, num in enumerate(nums):
      if num in dict_ and i - dict_[num] <=k:
        return True
      else:
        dict_[num] = i
    return False
