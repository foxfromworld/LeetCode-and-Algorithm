# Source : https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/
# Author : foxfromworld
# Date  : 10/12/2021
# First attempt

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count=0
        for i in range(0,len(s)-2):
            if s[i]!=s[i+1] and s[i+1]!=s[i+2] and s[i]!=s[i+2]:
                count=count+1
        return count
