# Source : https://leetcode.com/problems/merge-strings-alternately/
# Author : foxfromworld
# Date  : 07/11/2021
# Second attempt

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n, m = len(word1), len(word2)
        ret = ''
        for i in range(min(n, m)):
            ret += word1[i] + word2[i] 
        if n < m:
            return ret + word2[n:m]
        elif n > m:
            return ret + word1[m:n]
        else:
            return ret

# Date  : 07/11/2021
# First attempt

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n, m = len(word1), len(word2)
        ret = ''
        for i in range(min(n, m)):
            ret += word1[i] + word2[i] 
        if n < m:
            return ret + word2[(n-m):]
        elif n > m:
            return ret + word1[(m-n):]
        else:
            return ret
