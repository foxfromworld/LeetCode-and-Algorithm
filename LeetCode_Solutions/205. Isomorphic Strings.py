# Source : https://leetcode.com/problems/isomorphic-strings/
# Author : foxfromworld
# Date  : 11/03/2021
# First attempt 

class Solution:
  def isIsomorphic(self,s,t):
    return len(set(s))==len(set(t))==len(set(zip(s,t)))
