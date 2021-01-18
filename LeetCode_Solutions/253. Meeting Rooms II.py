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
    intervals.sort() # Sort the time slots by the start time
    heapq.heappush(heap, intervals[0][1]) # Initialize a min heap to keep the track of the next meeting
    for room in intervals[1:]:
      if room[0] >= heap[0]:
        heapq.heapreplace(heap, room[1]) # If the new one's start time is latter then the ending of the former one, replace it
      else:
        heapq.heappush(heap, room[1]) # If the time slots overlap, add the new one into the heap
    return len(heap)
