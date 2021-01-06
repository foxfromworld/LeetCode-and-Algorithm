# Source : https://leetcode.com/problems/intersection-of-two-arrays/
# Author : foxfromworld
# Date  : 20/11/2020

# Second attempt
class Solution:
  def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    nums1 = set(nums1)
    nums2 = set(nums2)
  return [ i for i in nums1 if i in nums2] # Create a list by comparing the two sets
  #return (nums1.intersection(nums2)) # Use built-in function

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
  
