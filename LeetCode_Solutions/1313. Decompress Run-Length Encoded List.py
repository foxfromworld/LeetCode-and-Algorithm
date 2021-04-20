# Source : https://leetcode.com/problems/decompress-run-length-encoded-list/
# Author : foxfromworld
# Date  : 20/04/2021
# First attempt

class Solution:
  def decompressRLElist(self, nums: List[int]) -> List[int]:
    returnL = []
    for i in range(0, len(nums), 2):
      freq, val = nums[i], nums[i+1]
      returnL += freq * [val]
    return returnL
