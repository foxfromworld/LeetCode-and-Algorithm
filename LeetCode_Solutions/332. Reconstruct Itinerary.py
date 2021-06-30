# Source : https://leetcode.com/problems/reconstruct-itinerary/
# Author : foxfromworld
# Date  : 30/06/2021
# First attempt 

import collections
class Solution(object):
  def findItinerary(self, tickets):
    """
    :type tickets: List[List[str]]
    :rtype: List[str]
    """            
    graph = collections.defaultdict(list)
    for st, ed in tickets:
      graph[st].append(ed)
    for st in graph:
      graph[st].sort()     
    stack = ['JFK']
    itinerery = []
    while stack:
      while graph[stack[-1]]:
        stack.append(graph[stack[-1]].pop(0))
      itinerery.append(stack.pop())
    return itinerery[::-1]
