# Source : https://leetcode.com/problems/evaluate-division/
# Author : foxfromworld
# Date  : 17/7/2021
# First attempt

from collections import defaultdict
class Solution(object):
  def calcEquation(self, equations, values, queries):
    """
    :type equations: List[List[str]]
    :type values: List[float]
    :type queries: List[List[str]]
    :rtype: List[float]
    """
    graph = defaultdict(defaultdict)
    result = []
    def dfs(curr_node, target_node, acc_product, visited):
      ret = -1.0
      next_nodes = graph[curr_node]
      visited.add(curr_node)
      if target_node in next_nodes:
        ret = acc_product * next_nodes[target_node]
      else:
        for next_node, val in next_nodes.items():
          if next_node in visited:
            continue
          ret = dfs(next_node, target_node, acc_product * val , visited)
          if ret != -1.0:
            break
      visited.remove(curr_node)
      return ret
    for (dividend, divisor) , value in zip(equations, values):
      graph[dividend][divisor] = value
      graph[divisor][dividend] = 1 / value
    for dividend, divisor in queries:
      if dividend not in graph or divisor not in graph:
        ret = -1.0
      elif dividend == divisor:
        ret = 1.0
      else:
        visited = set()
        ret = dfs(dividend, divisor, 1, visited)
      result.append(ret)
    return result
