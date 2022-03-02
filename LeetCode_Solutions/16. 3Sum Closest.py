# Source : https://leetcode.com/problems/3sum-closest/
# Author : foxfromworld
# Date   : 02/03/2022
# First attempt

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = float('-inf')                    
        for i in range(len(nums)):
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                sum_ = nums[lo] + nums[hi] + nums[i]
                if abs(target - sum_) < abs(diff):
                    diff = target - sum_
                if sum_ > target:
                    hi -= 1 
                else:
                    lo += 1
            if diff == 0: break
        return target - diff
