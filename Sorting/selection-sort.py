# Author : foxfromworld
# Date   : 23/11/2020

"""
  S = (n-1) + (n-2) + (n-3) + ... + 3 + 2 + 1
+ S = 1 + 2 + 3 + ... + (n-3) + (n-2) + (n-1)
---------------------------------------------------
 2S = n + n + ... + n 
     |←　 　n-1　　　→|
     
  S = n*(n-1)/2 = n**2 - n/2 ==> n**2
  
Worst-case performance:	О(n**2) comparisons, О(n) swaps
Best-case performance:	О(n**2) comparisons, O(1) swaps
Average performance:	О(n**2) comparisons, О(n) swaps
Worst-case space complexity: O(1) auxiliary
Stable: No (Same value will be swapped later)
"""

string = "SELECTIONSORT"
nums = [ ord(ch) for ch in string ]
print(nums)

def selection_sort(nums):
  for i in range(len(nums)):
    j = i+1
    min = i
    for j in range(j,len(nums)):
      if nums[min] > nums[j]:
        min = j
    nums[min], nums[i] = nums[i], nums[min]
  return nums
  
selection_sort(nums)
print(nums)
wordlist2 = [ chr(num) for num in nums ]
print(wordlist2)
