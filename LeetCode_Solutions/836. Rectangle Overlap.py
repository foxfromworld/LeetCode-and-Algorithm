# Source : https://leetcode.com/problems/rectangle-overlap/
# Author : foxfromworld
# Date  : 07/04/2021
# Second attempt

class Solution:
  def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:    
    if rec1[0] == rec1[2] or rec2[0] == rec2[2] or\
      rec2[1] == rec2[3] or rec1[1] == rec1[3]:
      return False
    UpBound = min(rec1[3], rec2[3])
    LoBound = max(rec1[1], rec2[1])
    RtBound = min(rec1[2], rec2[2])
    LtBound = max(rec1[0], rec2[0])

    return True if UpBound > LoBound and RtBound > LtBound else False

# Date  : 07/04/2021
# First attempt

class Solution:
  def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
    if rec1[0] == rec1[2] or rec1[1] == rec1[3] or \
      rec2[0] == rec2[2] or rec2[1] == rec2[3]:
      return False # check if it's a line
    return rec2[0] < rec1[2] and rec2[1] < rec1[3] and rec1[0] < rec2[2] and rec1[1] < rec2[3]
