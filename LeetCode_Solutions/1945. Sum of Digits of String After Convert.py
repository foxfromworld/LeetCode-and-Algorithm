# Source : https://leetcode.com/problems/sum-of-digits-of-string-after-convert/
# Author : foxfromworld
# Date  : 21/11/2021
# First attempt

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        newStr = ''
        for i in range(len(s)):
            newStr += str(alpha.index(s[i]) + 1)
        temp = list(newStr)
        ret = 0
        for _ in range(k):
          ret = sum([int(ch) for ch in temp])
          temp = list(str(ret))
        return ret
