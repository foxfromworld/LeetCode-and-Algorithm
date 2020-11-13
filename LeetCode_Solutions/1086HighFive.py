# Source : https://leetcode.com/problems/high-five/
# Author : foxfromworld
# Date  : 13/11/2020
# First attempt 

from typing import List
class Solution:
  def highFive(self, items: List[List[int]]) -> List[List[int]]:
    items = sorted(items, reverse = True)    
    cnt = sum = 0
    returnL = temp = []
    student = items[0][0]
    for i in range(len(items)):
      if student != items[i][0]:
        returnL.insert(0, [student, sum//5])
        student = items[i][0]
        temp = []
        cnt = 0
        sum = 0       
      if cnt<5 :
        sum += items[i][1]
        cnt += 1     
    returnL.insert(0, [student, sum//5])
    return returnL
