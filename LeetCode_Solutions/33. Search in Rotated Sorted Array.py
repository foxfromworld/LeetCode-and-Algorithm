# Source : https://leetcode.com/problems/search-in-rotated-sorted-array/
# Author : foxfromworld
# Date   : 14/03/2022
# First attempt

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        # 4  5  6  7  0  1  2
        # l        m        r
        while l <= r:
            m = (l + r) // 2
            print(m)
            if nums[m] == target: return m
            if nums[m] <= nums[r]: 
            # ▉▂▃▅▆▇
            # l   m     r                
                if target > nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            else:
            # ▆▇▉▂▃▅
            # l   m     r
                if target < nums[m] and target >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1
        return -1
