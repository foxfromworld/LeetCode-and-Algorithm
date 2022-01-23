# Source : https://leetcode.com/problems/sum-of-all-subset-xor-totals/
# Author : foxfromworld
# Date  : 23/01/2022
# Second attempt

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subsets = [[]]
        ret = 0
        for num in nums:
            subsets += [subset + [num] for subset in subsets]
        for l in subsets:
            x = 0            
            for i in l:
                x ^= i
            ret += x
        return ret
    
# Date  : 23/01/2022
# First attempt

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def helper(i):
            if i == len(nums):
                return [0]
            xors = helper(i+1)
            return xors + [nums[i] ^ xor for xor in xors]
        return sum(helper(0))
