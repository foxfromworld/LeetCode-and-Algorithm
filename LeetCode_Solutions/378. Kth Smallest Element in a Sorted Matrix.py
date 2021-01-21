# Source : https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
# Author : foxfromworld
# Date  : 21/01/2021
# First attempt 

class Solution:
  def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    newList = []
    for row in matrix:
      newList += row
    newList.sort()
    return newList[k-1]
