# Source : https://leetcode.com/problems/4sum/
# Author : foxfromworld
# Date   : 03/03/2022
# First attempt

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()  
        n = len(nums)
        ret = []
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                lo = j + 1
                hi = n - 1
                while lo < hi:
                    sum_ = nums[i] + nums[j] + nums[lo] + nums[hi]
                    if sum_ < target:
                        lo += 1
                    elif sum_ > target:
                        hi -= 1
                    else:
                        ret.append([nums[i], nums[j], nums[lo], nums[hi]])
                        lo += 1
                        hi -= 1
                        while lo < hi and nums[lo] == nums[lo - 1]:
                            lo += 1                            
        return ret
