# Source : https://leetcode.com/problems/detect-capital/
# Author : foxfromworld
# Date  : 12/12/2021
# Second attempt

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or (word[0].isupper() and word[1:].islower())

# Date  : 12/12/2021
# First attempt

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        ret = 0
        for ch in word:    
            if ch.isupper():
                ret += 1
        if ret == 1 and word[0].isupper():
            return True
        if ret == len(word):
            return True
        if ret == 0:
            return True
        else:
            return False
