# Source : https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/
# Author : foxfromworld
# Date  : 29/09/2021
# First attempt 

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        ret = 0
        for i, num in enumerate(nums):
            j = i + 1
            for nj in nums[j:]:
                if abs(nj - num) == k:
                    ret += 1
        return ret
