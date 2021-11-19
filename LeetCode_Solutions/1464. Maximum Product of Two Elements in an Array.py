# Source : https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/
# Author : foxfromworld
# Date  : 18/11/2021
# Third attempt

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        return (heapq.nlargest(2, nums)[0] - 1) * (heapq.nlargest(2, nums)[1] - 1)

# Date  : 18/11/2021
# Second attempt

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1] - 1) * (nums[-2] - 1) 

# Date  : 18/11/2021
# First attempt

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1, max2 = 0, 0
        for num in nums:
            if num > max1:
                max2, max1 = max1, num   
            elif num > max2:
                max2 = num
        return (max1 - 1) * (max2 - 1)
