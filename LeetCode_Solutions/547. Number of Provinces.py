# Source : https://leetcode.com/problems/number-of-provinces/submissions/
# Author : foxfromworld
# Date  : 12/06/2021
# First attempt (DFS)

class Solution(object):
  def findCircleNum(self, isConnected):
    """
    :type isConnected: List[List[int]]
    :rtype: int
    """    
    num = len(isConnected)
    visited = [0] * num
    group = 0
    def dfs(i):
      for j in range(num):
        if visited[j] != 1 and isConnected[i][j]:
          visited[j] = 1
          dfs(j)
    for i in range(num):
      if visited[i] != 1:
        dfs(i)
        group += 1
    return group 
