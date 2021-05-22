# Source : https://leetcode.com/problems/parallel-courses/
# Author : foxfromworld
# Date  : 20/05/2021
# Third attempt # DFS2

class Solution:
  def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
    graph = { v:[] for v in range(1, N+1)}
    for st, ed in relations:
      graph[st].append(ed)
    visit = {}
    def dfs(node):
      if node in visit:
        return visit[node]
      else:
        visit[node] = -1
      max_length = 1
      for end_node in graph[node]:
        length = dfs(end_node)
        if length == -1:
          return -1
        else:
          max_length = max(length + 1, max_length)
      visit[node] = max_length
      return max_length
    max_length = 1  
    for node in graph:
        length = dfs(node)
        if length == -1:
          return -1
        else:
          max_length = max(length, max_length)
    return max_length    

# Date  : 21/05/2021
# Second attempt # DFS1 (Find the longest path)

class Solution:
  def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
    graph = {v: [] for v in range(1, N + 1)}
    for st, ed in relations: # create the graph
      graph[st].append(ed)
    visit_status = {}
    def check_cycle(node): # check if there is a cyle
      if node in visit_status:
        return visit_status[node]
      else:
        visit_status[node] = -1
      for end_node in graph[node]:
        if check_cycle(end_node):
          return True
      visit_status[node] = False
      return False
    for node in graph:
      if check_cycle(node):
        return -1
    longest_path = {}
    def find_longest_path(node): # find the longest path
      if node in longest_path:
        return longest_path[node]
      max_length = 1
      for end_node in graph[node]:
        length = find_longest_path(end_node)
        max_length = max(length + 1, max_length)
      longest_path[node] = max_length
      return max_length
    return max(find_longest_path(node) for node in graph)

# Date  : 20/05/2021
# First attempt # BFS

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
