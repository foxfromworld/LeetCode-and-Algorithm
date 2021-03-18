# Source : https://leetcode.com/problems/product-of-array-except-self/
# Author : foxfromworld
# Date  : 18/03/2021
# First attempt 

class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    length = len(nums)
    lProd, rProd, ans = [1]*length, [1]*length, [0]*length
    for i in range(1, length):
      lProd[i] = lProd[i-1]*nums[i-1]
    for i in range(length-1-1, -1, -1):
      rProd[i] = rProd[i+1]*nums[i+1]    
    for i in range(length): 
      ans[i] = lProd[i]*rProd[i]
    return ans
