# Source : https://leetcode.com/problems/implement-strstr/
# Author : foxfromworld
# Date  : 07/10/2021
# Second attempt

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle: return 0
        length = len(needle)
        for i in range(len(haystack)):
            if haystack[i:i+length] == needle:
                return i
        return -1

# Date  : 07/10/2021
# First attempt

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
