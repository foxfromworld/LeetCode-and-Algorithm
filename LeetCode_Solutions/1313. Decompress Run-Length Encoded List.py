# Source : https://leetcode.com/problems/decompress-run-length-encoded-list/
# Author : foxfromworld
# Date  : 21/04/2021
# Fourth attempt

class Solution:
  def decompressRLElist(self, nums: List[int]) -> List[int]:
    returnL = []
    for i in range(0, len(nums), 2):
      returnL.append((f'{nums[i+1]},' * nums[i])[:-1])
    return returnL 

# Date  : 21/04/2021
# Third attempt

class Solution:
  def decompressRLElist(self, nums: List[int]) -> List[int]:
    returnL = []
    for i in range(0, len(nums), 2):
      returnL.append(((str(nums[i+1])+',') * nums[i])[:-1])
    return returnL 

# Date  : 20/04/2021
# Second attempt

class Solution:
  def decompressRLElist(self, nums: List[int]) -> List[int]:
    returnL = []
    i = 0
    while i < len(nums): 
      returnL += nums[i] * [nums[i+1]]
      i += 2
    return returnL 

# Date  : 20/04/2021
# First attempt

class Solution:
  def decompressRLElist(self, nums: List[int]) -> List[int]:
    returnL = []
    for i in range(0, len(nums), 2):
      freq, val = nums[i], nums[i+1]
      returnL += freq * [val]
    return returnL
