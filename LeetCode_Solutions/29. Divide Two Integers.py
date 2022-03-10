# Source : https://leetcode.com/problems/divide-two-integers/
# Author : foxfromworld
# Date   : 10/03/2022
# First attempt

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ret = 0
        isPositive = (dividend > 0) == (divisor > 0)
        dividend, divisor = abs(dividend), abs(divisor)
        while dividend >= divisor:
            powerofTwo, i = divisor, 1
            while dividend >= powerofTwo:
                dividend -= powerofTwo
                ret += i
                i <<= 1
                powerofTwo <<= 1
        if not isPositive:
            ret = -ret
        return min(max(-2147483648, ret), 2147483647)
