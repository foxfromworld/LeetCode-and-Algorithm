# Source : https://leetcode.com/problems/high-five/
# Author : foxfromworld
# Date  : 20/11/2020
# First attempt 

class Solution:
  def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    set1, set2 = set(nums1), set(nums2)
    returnL = []
    if (len(set1)) > (len(set2)):
      set1, set2 = set2, set1 
    new_dict = dict.fromkeys(set1,0)
    for key in new_dict:
      if key in set2:
        returnL.append(key)
    return returnL
