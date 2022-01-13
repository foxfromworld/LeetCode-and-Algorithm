# Source : https://leetcode.com/problems/palindrome-permutation/
# Author : foxfromworld
# Date  : 12/01/2022
# First attempt

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        seen = set()
        for ch in s:
            if ch not in seen:
                seen.add(ch)
            else:
                seen.remove(ch)
        return len(seen) <= 1
