# Source : https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/
# Author : foxfromworld
# Date  : 30/11/2021
# First attempt

class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        curr = 0
        for token in s.split(' '):
            if token.isdigit():
            #if token.isnumeric():
                token = int(token)
                if token > curr:
                    curr = token
                else:
                    return False
        return True if curr > 0 else False
