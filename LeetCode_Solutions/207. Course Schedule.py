# Source : https://leetcode.com/problems/course-schedule/ (Similiar to 1136	Parallel Courses)
# Author : foxfromworld
# Date  : 06/06/2021
# Third attempt (DFS)

class Solution(object):
  def canFinish(self, numCourses, prerequisites):
    graph = {v:[] for v in range(numCourses)}
    for ed, st in prerequisites:
      graph[st].append(ed)
    visit_status = {} # -1: visiting; False: visited
    def isCyclic(node):
      if node not in visit_status:
        visit_status[node] = -1
      else:
        return visit_status[node]
      for end_node in graph[node]:
        if isCyclic(end_node):
          return True
      visit_status[node] = False
      return False
    for node in graph:
      if isCyclic(node):
        return False
    return True

# Date  : 06/06/2021
# Second attempt (Topological Sort)

class Solution(object):
  def canFinish(self, numCourses, prerequisites):
    graph = {v:[] for v in range(numCourses)}
    edge = {v:0 for v in range(numCourses)}
    queue = []

    for ed, st in prerequisites: ##### Modified
      graph[st].append(ed) 
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
