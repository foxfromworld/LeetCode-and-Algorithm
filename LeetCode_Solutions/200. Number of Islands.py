# Source : https://leetcode.com/problems/number-of-islands/
# Author : foxfromworld
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
