# Source : https://leetcode.com/problems/kth-largest-element-in-an-array/
# Author : foxfromworld
# Date  : 16/01/2021
# Third attempt 

class Solution:
  def findKthLargest(self, nums: List[int], k: int) -> int:               
    return heapq.nlargest(k, nums)[-1]
    # nlargest: descending
    # nsmallest: ascending

# Date  : 16/01/2021
# Second attempt 

class Solution:
  def findKthLargest(self, nums: List[int], k: int) -> int:               
    nums.sort()
    return nums[-k]

# Date  : 16/01/2021
# First attempt 

# The idea is to keep the K largest elements in a heap

class Solution:
  def findKthLargest(self, nums: List[int], k: int) -> int:               
    heapq.heapify(nums)
    while len(nums) > k:
      heapq.heappop(nums)
    return nums[0]
