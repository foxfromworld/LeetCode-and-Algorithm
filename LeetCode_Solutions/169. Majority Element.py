# Source : https://leetcode.com/problems/majority-element/
# Author : foxfromworld
# Date  : 20/02/2022
# Second attempt # Boyer–Moore majority vote algorithm

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == prev:
                count += 1
            elif nums[i] != prev:
                count -= 1
                if count == 0:
                    prev = nums[i]
                    count = 1
        return prev

# Date  : 20/02/2022
# First attempt

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = len(nums) // 2
        dict_ = defaultdict(int)
        for e in nums:
            dict_[e] += 1
            if dict_[e] > freq:
                return e
