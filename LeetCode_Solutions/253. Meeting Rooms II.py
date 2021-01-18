# Source : https://leetcode.com/problems/meeting-rooms-ii/
# Author : foxfromworld
# Date  : 18/01/2021
# First attempt 

import heapq
class Solution:
  def minMeetingRooms(self, intervals: List[List[int]]) -> int:
    if len(intervals) < 1:
      return 0
    heap = []
    intervals.sort()
    heapq.heappush(heap, intervals[0][1])
    for room in intervals[1:]:
      if room[0] >= heap[0]:
        heapq.heapreplace(heap, room[1])
      else:
        heapq.heappush(heap, room[1])
    return len(heap)
