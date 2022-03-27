# Source : https://leetcode.com/problems/summary-ranges/
# Author : foxfromworld
# Date   : 27/03/2022
# First attempt

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        ret = []
        i = 0
        for j in range(n):
            if j < i: continue
            while j + 1 < n and nums[j] + 1 == nums[j + 1]:
                j += 1
            if i == j:
                ret.append(str(nums[i]))
            else:
                ret.append(str(nums[i]) + "->" + str(nums[j]))
            i = j + 1
        return ret
