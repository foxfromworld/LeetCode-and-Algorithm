# Source : https://leetcode.com/problems/integer-to-roman/
# Author : foxfromworld
# Date  : 03/01/2021
# Second attempt

class Solution:
    def intToRoman(self, num: int) -> str:
        table = [['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'], ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'], ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'], ['', 'M', 'MM', 'MMM']]
        ret = ''
        digit = 0
        while num > 0:
            ret = table[digit][num % 10] + ret
            num //= 10
            digit += 1
        return ret

# Date  : 03/01/2021
# First attempt

class Solution:
    def intToRoman(self, num: int) -> str:
        table = [1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'], [100,'C'], [90, 'XC'], [50, 'L'], [40, 'XL'], [10, 'X'], [9, 'IX'], [5, 'V'], [4, 'IV'], [1, 'I']
        ret = ''
        index = 0
        while num > 0:
            if num - table[index][0] < 0:
                index += 1
            else:
                num -= table[index][0]
                ret += table[index][1]
        return ret
