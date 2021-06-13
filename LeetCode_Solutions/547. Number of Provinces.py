# Source : https://leetcode.com/problems/number-of-provinces/
# Author : foxfromworld
# Date  : 13/06/2021
# Second attempt (BFS)

class Solution(object):
  def findCircleNum(self, isConnected):
    num = len(isConnected)
    visited = [0] * num
    group = 0
    for i in range(num):
      if visited[i] != 1:
        from collections import deque
        queue = deque([i])
        while queue:
          node = queue.popleft()
          visited[node] = 1
          for j in range(num):
            if isConnected[node][j] == 1 and visited[j] != 1:
              queue.append(j)
        group += 1
    return group

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
