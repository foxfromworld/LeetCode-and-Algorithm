# Source : https://leetcode.com/problems/lemonade-change/
# Author : foxfromworld
# Date  : 20/11/2021
# First attempt

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        tenner, fiver, twenty = 0, 0, 0
        for bill in bills:
            if bill == 5:
                fiver += 1
            elif bill == 10:
                if not fiver:
                    return False
                fiver -= 1
                tenner += 1
            else:
                if fiver and tenner:
                    tenner -= 1
                    fiver -= 1
                    twenty += 1
                elif fiver >= 3:
                    fiver -=3
                    twenty += 1
                else:
                    return False
        return True
