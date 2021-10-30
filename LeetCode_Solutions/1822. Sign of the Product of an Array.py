# Source : https://leetcode.com/problems/sign-of-the-product-of-an-array/
# Author : foxfromworld

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ret = 1
        for num in nums:
            if num == 0:
                return 0
            elif num < 0:
                ret *= -1
        return ret

# Date  : 30/10/2021
# First attempt

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        neg_cnt = 0
        for num in nums:
            if num == 0:
                return 0
            elif num < 0:
                neg_cnt += 1
        return 1 if neg_cnt % 2 == 0 else -1
