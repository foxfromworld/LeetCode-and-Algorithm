# Source : https://leetcode.com/problems/happy-number/
# Author : foxfromworld
# Date   : 10/06/2022
# First attempt

class Solution:
    def isHappy(self, n: int) -> bool:
        def calculateNext(num):
            newNum = 0
            while num > 0:
                digit = num % 10
                num //= 10
                newNum += digit*digit
            return newNum
        slow = n
        fast = calculateNext(n)
        while slow != fast and fast != 1:
            slow = calculateNext(slow)
            fast = calculateNext(calculateNext(fast))
        return fast == 1
