# Source : https://leetcode.com/problems/longest-common-prefix/
# Author : foxfromworld
# Date  : 04/10/2021
# First attempt 

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)
        result = ""
        char = set()
        for i in range(len(strs[0])):
            for j in range(len(strs)):
                char.add(strs[j][i])
            if len(char) > 1:
                return result
            else:
                result = result + strs[0][i]
            char.clear()
        return result
