# Source : https://leetcode.com/problems/subarray-sum-equals-k/
# Author : foxfromworld
# Date  : 10/02/2022
# First attempt

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_ = 0
        map_ = {0:1} # one zero
        ret = 0
        for num in nums:
            sum_ += num
            if sum_ - k in map_:
                ret += map_[sum_ - k]
            if sum_ in map_: map_[sum_] += 1
            else: map_[sum_] = 1
        return ret
