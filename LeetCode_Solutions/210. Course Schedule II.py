# Source : https://leetcode.com/problems/course-schedule-ii/
# Author : foxfromworld
# Date  : 13/07/2021
# First attempt (BFS)

class Solution(object):
  def findOrder(self, numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: List[int]
    """
    if numCourses == 1: return [0]
    graph = {i:[] for i in range(numCourses)}
    in_edge = {i:0 for i in range(numCourses)}
    queue = []
    for end, start in prerequisites:
      graph[start].append(end)
      in_edge[end] += 1
    for end in in_edge:
      if in_edge[end] == 0:
        queue.append(end)
    order, count = [], 0
    while queue:
      node = queue.pop(0)
      count += 1
      order.append(node)
      for end in graph[node]:
        in_edge[end] -= 1
        if in_edge[end] == 0:
          queue.append(end)
    return order if count == numCourses else []
