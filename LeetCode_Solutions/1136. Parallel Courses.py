# Source : https://leetcode.com/problems/parallel-courses/
# Author : foxfromworld
# Date  : 20/05/2021
# First attempt 

class Solution:
  def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
    graph = { v: [] for v in range(1, N+1)}  
    in_edge = { v: 0 for v in range(1, N+1)}  
    queue = []

    for st, ed in relations: # create the graph using the relations
      graph[st].append(ed)
    for st, ed in relations: # count the in edges using the relations
      in_edge[ed] += 1
    for ed in in_edge:
      if in_edge[ed] == 0:
        queue.append(ed)

    semester = 0
    studied = 0

    while queue:
      semester += 1
      next_queue = []
      for v in queue:
        studied += 1
        for end_node in graph[v]:
          in_edge[end_node] -= 1
          if in_edge[end_node] == 0:
            next_queue.append(end_node)
      queue = next_queue
    
    return semester if studied == N else -1
