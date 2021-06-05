# Source : https://leetcode.com/problems/course-schedule/ (Similiar to 1136	Parallel Courses)
# Author : foxfromworld
# Date  : 05/06/2021
# First attempt (Topological Sort)

class Solution(object):
  def canFinish(self, numCourses, prerequisites):
    graph = {v:[] for v in range(numCourses)}
    edge = {v:0 for v in range(numCourses)}
    queue = []

    for ed, st in prerequisites:
      graph[st].append(ed)    
    for ed, _ in prerequisites:
      edge[ed] += 1
    for ed in edge:
      if edge[ed] == 0:
        queue.append(ed)

    studied = 0

    while queue:
      next_queue = []
      for node in queue:
        studied += 1
        for end_node in graph[node]:
          edge[end_node] -= 1
          if edge[end_node] == 0:
            next_queue.append(end_node)
      queue = next_queue
    return True if studied == numCourses else False
