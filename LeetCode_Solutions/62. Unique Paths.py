# Source : https://leetcode.com/problems/unique-paths/
# Author : foxfromworld
# Date  : 25/10/2021
# First attempt 

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n] * m
        for mm in range(1, m):
            for nn in range(1, n):
                dp[mm][nn] = dp[mm-1][nn] + dp[mm][nn-1]
        return dp[-1][-1]
