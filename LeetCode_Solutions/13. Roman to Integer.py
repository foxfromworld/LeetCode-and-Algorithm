# Source : https://leetcode.com/problems/roman-to-integer/
# Author : foxfromworld
# Date  : 01/10/2021
# Second attempt

class Solution:
    def romanToInt(self, s: str) -> int:
        table = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        ret = 0
        for i in range(len(s)-1):
            if table[s[i]] < table[s[i+1]]:
                ret -= table[s[i]]
            else:
                ret += table[s[i]]           
        return ret + table[s[-1]]
                
# Date  : 01/10/2021
# First attempt

class Solution:
    def romanToInt(self, s: str) -> int:
        table = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        ret = 0
        for i, ch in enumerate(s):
            if i + 1 < len(s):
                if table[ch] < table[s[i+1]]:
                    ret -= table[ch]
                else:
                    ret += table[ch]
            else:
                ret += table[ch]
        return ret
