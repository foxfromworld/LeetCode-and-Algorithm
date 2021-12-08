# Source : https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/
# Author : foxfromworld
# Date  : 08/11/2021
# Second attempt

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        i = 0
        nums.sort()
        while i < len(nums) and nums[i] < 0 and i < k:
            nums[i] = -nums[i]
            i += 1
        return sum(nums) - (k - i) % 2 * min(nums) * 2
      
# Date  : 08/11/2021
# First attempt

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        i = 0
        nums.sort()
        while i < len(nums) and nums[i] < 0 and i < k:
            nums[i] = -nums[i]
            i += 1
        if (k - i) % 2 == 0: return sum(nums)
        else:
            return sum(nums) - min(nums) - min(nums) # sum(nums) includes the nums[i] that will be modified as -nums[i], so we need to remove it      
