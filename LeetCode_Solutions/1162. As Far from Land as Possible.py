# Source : https://leetcode.com/problems/as-far-from-land-as-possible/
# Author : foxfromworld
# Date  : 06/07/2021
# First attempt 

from collections import deque
class Solution(object):
  def maxDistance(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    d = 0
    size = len(grid)
    queue = deque([(x, y) for x in range(size) for y in range(size) if grid[x][y] == 1])
    if len(queue) == size*size: return -1 
    while queue:
      num = len(queue)
      for _ in range(num):
        x, y = queue.popleft()
        for x_, y_ in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
          if 0 <= x_ < size and 0 <= y_ < size and grid[x_][y_] == 0:
            queue.append((x_, y_))
            grid[x_][y_] = 1
      d += 1
    return d - 1 
