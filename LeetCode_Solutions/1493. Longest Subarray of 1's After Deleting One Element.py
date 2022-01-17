# Source : https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/
# Author : foxfromworld
# Date  : 17/01/2022
# First attempt

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if nums[0] == 1: nums.insert(0, 0)
        if nums[-1] == 1: nums.append(0)
        copy = nums.copy()
        zero = [0]
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
            if copy[i] == 0:
                zero.append(nums[i])
        ret = 0
        for i in range(1, len(zero)-1):
            ret = max(ret, zero[i] - zero[i-1] + zero[i+1] - zero[i])
        else:
            ret = max(ret, zero[1] - zero[0])
        if zero[-1] == n: return n-1
        if zero[-1] == 0: return 0
        return ret
