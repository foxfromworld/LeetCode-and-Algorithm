# Source : https://leetcode.com/problems/kth-largest-element-in-a-stream/
# Author : foxfromworld
# Date  : 15/01/2021
# First attempt 

# The idea is to keep the K largest elements in a heap

import heapq

class KthLargest:
  def __init__(self, k: int, nums: List[int]):
    self.heap = nums
    heapq.heapify(self.heap)
    self.k = k
    while len(self.heap) > k:
      heapq.heappop(self.heap)
  def add(self, val: int) -> int:
    if len(self.heap) < self.k:
      heapq.heappush(self.heap, val)
    elif val > self.heap[0]:
      heapq.heapreplace(self.heap, val)
    return self.heap[0]
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
