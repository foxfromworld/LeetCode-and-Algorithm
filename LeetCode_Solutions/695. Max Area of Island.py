# Source : https://leetcode.com/problems/max-area-of-island/
# Author : foxfromworld
# Date  : 27/05/2021
# Third attempt (recursive)

class Solution:
  def maxAreaOfIsland(self, grid):
    visit = set()
    def dfs(r, c):
      if not (0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] and not (r, c) in visit):
        return 0
      visit.add((r, c))
      return (1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1))
    return max(dfs(row, col) for row in range(len(grid)) for col in range(len(grid[0])))

# Date  : 26/05/2021
# Second attempt (iterative)

class Solution:
  def maxAreaOfIsland(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    visit = set()
    area = 0
    grid_row = len(grid)
    grid_col = len(grid[0])
    for row in range(grid_row):
      for col in range(grid_col):
        if grid[row][col] and not (row, col) in visit:
          stack = [[row, col]]
          visit.add((row, col))
          island = 0
          while stack:
            r, c = stack.pop()
            island += 1
            for d_row, d_col in (r,c+1),(r,c-1),(r+1,c),(r-1,c):
              if (0 <= d_row < grid_row and 0 <= d_col < grid_col 
                and grid[d_row][d_col] and not (d_row, d_col) in visit):
                stack.append([d_row, d_col])
                visit.add((d_row, d_col))
          area = max(area, island)
    return area

# Date  : 26/05/2021
# First attempt 

class Solution(object):
  def maxAreaOfIsland(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    visit = set()
    area = 0
    grid_row = len(grid)
    grid_col = len(grid[0])
    for row in range(grid_row):
      for col in range(grid_col):
        if grid[row][col] and not (row, col) in visit:
          print(grid[row][col], row, col) 
          stack = [(row, col)]
          visit.add((row, col))
          island = 0
          while stack:
            new_row, new_col = stack.pop()
            island += 1
            for d_row, d_col in ((0,1),(0,-1),(1,0),(-1,0)):
              adj_row = new_row + d_row
              adj_col = new_col + d_col
              if 0 <= adj_row < grid_row and 0 <= adj_col < grid_col and grid[adj_row][adj_col] and not (adj_row, adj_col) in visit:
                stack.append((adj_row, adj_col))
                visit.add((adj_row, adj_col))
          area = max(area, island)
    return area 
