# Source : https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Author : foxfromworld
# Date  : 03/10/2021
# Second attempt

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = {}
        i, ret = 0, 0
        for j in range(len(s)):
            if s[j] in visited:
                i = max(i, visited[s[j]])
            ret = max(j - i + 1, ret)
            visited[s[j]] = j + 1
        return ret

# Date  : 03/10/2021
# First attempt

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        dp = [0 for _ in range(len(prices))]
        
        for _ in range(1, 2+1):
            pos = -prices[0]
            profit = 0
            for i in range(1, len(prices)):
                pos = max(pos, dp[i]-prices[i])
                profit = max(profit, pos+prices[i])
                dp[i] = profit
        return profit
