# Source : https://leetcode.com/problems/string-to-integer-atoi/
# Author : foxfromworld
# Date  : 28/02/2022
# Second attempt

class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        ret = 0
        index = 0
        n = len(s)        
        lowBound = -2147483648 # -2^31
        upBound = 2147483647 # 2^31 - 1      
        
        while index < n and s[index] == ' ': 
            index += 1
        if index < n and s[index] == '-':
            sign = -1
            index += 1
        elif index < n and s[index] == '+':
            index += 1
        for i in range(index, n):
            if not s[i].isdigit():
                break
            digit = int(s[i])
            ret = ret * 10 + digit
            if ret > upBound or ret < lowBound: 
                return upBound if sign == 1 else lowBound            
        return ret * sign
      
# Date  : 28/02/2022
# First attempt

class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        lowBound = -2147483648 # -2^31
        upBound = 2147483647 # 2^31 - 1
        digits = ''
        index = 0
        n = len(s)
        while index < n and s[index] == ' ': 
            index += 1
        if index < n and s[index] == '-':
            sign = -1
            index += 1
        elif index < n and s[index] == '+':
            index += 1
        for i in range(index, n):
            if not s[i].isdigit():
                break
            digits += s[i]
        if digits =='': return 0
        ret = int(digits) * sign
        if ret > upBound:
            ret = upBound
        elif ret < lowBound:
            ret = lowBound
        return ret
