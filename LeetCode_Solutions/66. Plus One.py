# Source : https://leetcode.com/problems/plus-one/
# Author : foxfromworld
# Date  : 10/10/2021
# First attempt 

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result, carry = [], 0
        for i in range(len(digits)-1,-1,-1):
            if len(digits)-1 == i:
                digits[i] = 1 + carry + digits[i]
            else:
                digits[i] += carry 
            if digits[i] > 9:
                digits[i] -= 10
                carry = 1
            else:
                carry = 0
            result.append(digits[i])
        if carry > 0:
            result.append(carry)
        result.reverse()
        return result
