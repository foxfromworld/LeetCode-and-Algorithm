# Source : https://leetcode.com/problems/shuffle-the-array/
# Author : foxfromworld
# Date  : 20/11/2021
# First attempt

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ret = []
        for i in range(n):
            ret.append(nums[i])
            ret.append(nums[i+n])
        return ret
