# Source : https://leetcode.com/problems/replace-all-digits-with-characters/
# Author : foxfromworld
# Date  : 04/11/2021
# Second attempt 

class Solution:
    def replaceDigits(self, s: str) -> str:
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        ret = ''
        for i in range(1, len(s), 2):
            ret = ret + s[i-1] + alpha[int(s[i]) + alpha.index(s[i-1])]
        if len(s) % 2 != 0:
            ret += s[-1]
        return ret
            
        
# Date  : 04/11/2021
# First attempt 

class Solution:
    def replaceDigits(self, s: str) -> str:
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        ret, ch = s[0], s[0]
        for i in range(1, len(s)):
            if s[i] in '0123456789':
                ret += alpha[alpha.find(ch) + int(s[i])]
            if s[i] in alpha:
                ch = s[i]
                ret += ch
        return ret
