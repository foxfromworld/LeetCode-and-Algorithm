# Source : https://leetcode.com/problems/3sum/
# Author : foxfromworld
# Date   : 02/03/2022
# First attempt

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []
        def twoPointers(i, nums):
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                sum_ = nums[lo] + nums [hi] + nums[i]
                if sum_ < 0:
                    lo += 1
                elif sum_ > 0:
                    hi -= 1
                else:
                    ret.append([nums[lo], nums [hi], nums[i]])        
                    lo += 1
                    hi -= 1
                    while lo < hi and nums[lo] == nums[lo - 1]:
                        lo += 1
        for i in range(len(nums)):
            if nums[i] > 0: break
            if i == 0 or nums[i] != nums[i-1]:
                twoPointers(i,  nums)
        return ret 
