# Source : https://leetcode.com/problems/longest-palindromic-substring/
# Author : foxfromworld
# Date  : 25/02/2022
# First attempt

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s[::-1] == s[:]: return s
        idx, size = 0, 1
        for i in range(1, len(s)):
            left, right = i - size , i + 1
            s_center, s_orig = s[left - 1:right], s[left:right]
            if left >= 1 and s_center[:] == s_center[::-1]:
                idx, size = left-1, size + 2
            elif s_orig[:] == s_orig[::-1]:
                idx, size = left, size + 1
        return s[idx:idx+size]
