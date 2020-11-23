# Author : foxfromworld
# Date   : 15/11/2020

"""

  S = (n-1) + (n--1-1) + ... + 3 + 2 + 1 = (n-1) + (n-2) + ... + 3 + 2 + 1
+ S = 1 + 2 + 3 + ... + (n-3) + (n-2) + (n-1)
---------------------------------------------------
 2S = n + n + ... + n 
     |←　 　n-1　　　→|
     
  S = n*(n-1)/2 = n**2 - n/2 ==> n**2
  
Worst-case performance:	O(n**2) comparisons, O(n**2) swaps
Best-case performance: O(n) comparisons, O(1) swaps
Average performance: O(n**2) comparisons, O(n^2) swaps
Worst-case space complexity: O(n) total, O(1) auxiliary
Stable: Yes (when two compared elements are the same, they won't swap)
"""

def bubble_sort(nums):
  for i in range(len(nums)-1,0,-1):
    for j in range(i):
      if nums[j] > nums[j+1]: # exchange every two elements i rounds, and each round takes j steps to complete the swaps
        nums[j],nums[j+1] = nums[j+1],nums[j]
  return nums
