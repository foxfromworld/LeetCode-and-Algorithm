# Source : https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/submissions/
# Author : foxfromworld
# Date  : 29/12/2020
# First attempt 

class Solution:
  def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
    returnL =[]
    for x in range(1,1000):# Loop over 1 ≤ x,y ≤ 1000 and check if f(x,y) == z.
      if customfunction.f(x,1)>z: break
      end = 1000
      start = 1
      while end>start:# Binary search
        mid = (start+end)//2
        temp = customfunction.f(x,mid)
        if temp==z:
          returnL.append(x,mid)
          break
        elif temp>z:
          end = mid
        elif temp<z:
          start = mid+1
    return returnL  
