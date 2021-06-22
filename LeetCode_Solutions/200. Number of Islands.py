# Source : https://leetcode.com/problems/number-of-islands/
# Author : foxfromworld
# Date  : 22/06/2021
# Third attempt

class Solution(object):
  def numIslands(self, grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    if not grid: return 0
    row, col = len(grid), len(grid[0])
    visit = set()
    count = 0
    for rw in range(row):
      for cl in range(col):
        if (rw, cl) not in visit and grid[rw][cl] == '1':
          count += 1
          from collections import deque
          queue = deque([(rw, cl)])
          visit.add((rw, cl))
          while queue:
            r, c = queue.popleft()
            for adj_r, adj_c in (r+1, c), (r-1, c), (r, c+1), (r, c-1):
              if 0 <= adj_r < row and 0 <= adj_c < col and grid[adj_r][adj_c] == '1' and (adj_r, adj_c) not in visit:
                visit.add((adj_r, adj_c))
                queue.append((adj_r, adj_c))
    return count  

# Date  : 19/06/2021
# Second attempt

class Solution(object):
  def numIslands(self, grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    if not grid: return 0
    row, col = len(grid), len(grid[0])
    visit = set()
    count = 0
    def dfs(r, c):
      if (r, c) in visit or r < 0 or r >= row or c < 0  or c >= col or grid[r][c] == '0':
        return
      visit.add((r, c))
      dfs(r+1, c)
      dfs(r-1, c)
      dfs(r, c+1)
      dfs(r, c-1)
    for rw in range(row):
      for cl in range(col):
        if (rw, cl) not in visit and grid[rw][cl] == '1':
          count += 1
          dfs(rw, cl)
    return count

# Date  : 19/06/2021
# First attempt (DFS)

class Solution(object):
  def numIslands(self, grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    if not grid: return 0
    row, col = len(grid), len(grid[0])
    visit = set()
    count = 0
    def dfs(r, c):
      if (r, c) not in visit and grid[r][c] == '1':
        visit.add((r, c))
        for adj_r, adj_c in (r+1, c), (r-1, c), (r, c+1), (r, c-1):
          if 0 <= adj_r < row and 0 <= adj_c < col:
            dfs(adj_r, adj_c)
    for rw in range(row):
      for cl in range(col):
        if (rw, cl) not in visit and grid[rw][cl] == '1':
          count += 1
          dfs(rw, cl)
    return count
