# Author : foxfromworld
# Date   : 12/11/2020

"""
  S = (n-1) + (n-2) + (n-3) + ... + 3 + 2 + 1
+ S = 1 + 2 + 3 + ... + (n-3) + (n-2) + (n-1)
---------------------------------------------------
 2S = n + n + ... + n 
     |←　 　n-1　　　→|
     
  S = n*(n-1)/2 = n**2 - n/2 ==> n**2
  
Worst-case performance: О(n**2) comparisons and swaps
Best-case performance: O(n) comparisons, O(1) swaps
Average performance: О(n**2) comparisons and swaps
Worst-case space complexity: О(n) total, O(1) auxiliary
Stable: Yes (when two compared elements are the same, they won't swap)
"""

def insertion_sort(nums):
  for i in range(len(nums)):
    # nums[i] is the newest element to be checked
    j = i # use j to check where to insert the newest element in the sorted part
    while (j>0) and nums[j-1]>nums[j] : 
      nums[j-1], nums[j] = nums[j], nums[ j-1] # swap the two elements
      j -= 1 # start checking from the last element of the sorted part
