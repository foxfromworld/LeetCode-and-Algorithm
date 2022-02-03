# Source : https://leetcode.com/problems/subsets/
# Author : foxfromworld
# Date  : 02/03/2022
# Second attempt

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        def backtrack(start = 0, curr = []):
            if len(curr) == i:
                output.append(curr[:])
                return
            for j in range(start, n):
                curr.append(nums[j])
                backtrack(j + 1, curr)
                curr.pop()
        output = []
        for i in range(n + 1): # include null
            backtrack()
        return output

# Date  : 02/02/2022
# First attempt

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        for num in nums:
            output += [[num] + sub for sub in output]
        return output
