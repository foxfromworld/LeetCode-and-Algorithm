# Source : https://leetcode.com/problems/missing-ranges/
# Author : foxfromworld
# Date  : 29/11/2020
# Second attempt 

class Solution:
  def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
    def findrange(low,high):
      if low==high:
        return [str(low)]
      else:
        return [str(low)+"->"+str(high)]
    returnL =[]
    if len(nums)==0:
      print("test")
      return findrange(lower,upper)
    for i in range(len(nums)-1): 
      if nums[i+1]-nums[i]>1:
        returnL+=findrange(nums[i]+1,nums[i+1]-1)
    if nums[0]!=lower: # deal with the beginning
      returnL= findrange(lower,nums[0]-1) + returnL
    if upper!=nums[-1]: # deal with the end
      returnL+=findrange(nums[-1]+1,upper)
    return returnL
