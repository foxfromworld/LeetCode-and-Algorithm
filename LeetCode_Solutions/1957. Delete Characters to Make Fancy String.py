# Source : https://leetcode.com/problems/delete-characters-to-make-fancy-string/
# Author : foxfromworld
# Date  : 12/02/2022
# Second attempt

class Solution:
    def makeFancyString(self, s: str) -> str:
        ret = ""
        isSecond = False
        lastCh = ""
        for ch in s:
            if lastCh == ch:
                if not isSecond:
                    isSecond = True
                    ret += ch 
            else:
                isSecond = False
                lastCh = ch
                ret += ch 
        return ret

# Date  : 12/02/2022
# First attempt

class Solution:
    def makeFancyString(self, s: str) -> str:
        dict_ = {}
        ret = ''
        for i, ch in enumerate(s):
            if i > 0 and ch == s[i - 1]:
                dict_[ch] += 1
            else:
                dict_[ch] = 1
            if dict_[ch] < 3:
                ret += ch
        return ret
