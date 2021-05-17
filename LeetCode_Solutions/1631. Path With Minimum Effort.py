# Source : https://leetcode.com/problems/path-with-minimum-effort/
# Author : foxfromworld
# Date  : 17/05/2021
# Second attempt

# Date  : 17/05/2021
# First attempt (Dijkstra's Algorithm)
"""

      col0  col1  col2
    ┌─────┬─────┬─────┐
row0│  1  │  2  │  2  │
    │(0,0)│(0,1)│(0,2)│
    ├─────┼─────┼─────┤
row1│  3  │  8  │  2  │
    │(1,0)│(1,1)│(1,2)│
    ├─────┼─────┼─────┤
row2│  5  │  3  │  5  │
    │(2,0)│(2,1)│(2,2)│
    └─────┴─────┴─────┘

Min heap
max_difference, x, y

Initial
---------------------
(0, 0, 0)

Visit (0, 0)
---------------------
(1, 0, 1)
(2, 1, 0)

Visit (0, 1)
---------------------
(1, 0, 2)
(2, 1, 0)
(6, 1, 1)

Visit (0, 2)
---------------------
(1, 1, 2)
(2, 1, 0)
(6, 1, 1)

Visit (1, 2)
---------------------
(2, 1, 0)
(3, 2, 2)
(6, 1, 1)

Visit (1, 0)
---------------------
(2, 2, 0)
(3, 2, 2)
(5, 1, 1)
(6, 1, 1)

Visit (2, 0)
---------------------
(2, 2, 1)
(3, 2, 2)
(5, 1, 1)
(6, 1, 1)

Visit (2, 1)
---------------------
(2, 2, 2)
(3, 2, 2)
(5, 1, 1)
(6, 1, 1)

Visit (2, 2)
---------------------
(3, 2, 2)
(5, 1, 1)
(6, 1, 1)

Visit (1, 1)
---------------------
(6, 1, 1)

Difference 
      col0  col1  col2
    ┌─────┬─────┬─────┐
row0│  0  │  1  │  1  │
    │(0,0)│(0,1)│(0,2)│
    ├─────┼─────┼─────┤
row1│  2  │  5  │  1  │
    │(1,0)│(1,1)│(1,2)│
    ├─────┼─────┼─────┤
row2│  2  │  2  │  2  │
    │(2,0)│(2,1)│(2,2)│
    └─────┴─────┴─────┘
"""
class Solution:
  def minimumEffortPath(self, heights: List[List[int]]) -> int:
    rw = len(heights)
    cl = len(heights[0])
    difference = [[float('inf')] * cl for _ in range(rw)]
    difference[0][0] = 0 # set the first element
    visited = [[False] * cl for _ in range(rw)] 
    minheap = [(0, 0, 0)]
    while minheap:
      _, row, col = heapq.heappop(minheap)
      visited[row][col] = True # traverse the first element
      for d_row, d_col in [0, 1], [1, 0], [0, -1], [-1, 0]: # access neighbors
        adj_row = row + d_row
        adj_col = col + d_col
        if 0 <= adj_row < rw and 0 <= adj_col < cl and not visited[adj_row][adj_col]:
          high_diff = abs(heights[row][col] - heights[adj_row][adj_col])
          # calculate the difference of the heights
          max_diff = max(high_diff, difference[row][col])
          # find the bigger needed effort
          if difference[adj_row][adj_col] > max_diff:
            difference[adj_row][adj_col] = max_diff
            # if the difference is 'inf' or bigger
            heapq.heappush(minheap, (max_diff, adj_row, adj_col))
    return difference[-1][-1]
