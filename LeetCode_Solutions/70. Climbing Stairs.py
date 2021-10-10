# Source : https://leetcode.com/problems/climbing-stairs/
# Author : foxfromworld
# Date  : 10/10/2021
# Second attempt 

class Solution:
    def climbStairs(self, n: int) -> int:
        f1, f2 = 1, 2
        for _ in range(n-1):
            f1, f2 = f2, f1 + f2
        return f1
      
# Date  : 10/10/2021
# First attempt 

class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3: return n
        dp = [0] * (n)
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i-2] + dp[i-1]
        return dp[-1]
