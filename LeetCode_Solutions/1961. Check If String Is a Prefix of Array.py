# Source : https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/
# Author : foxfromworld
# Date  : 09/11/2021
# Second attempt

class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        index = 0
        for word in words:
            length = len(word)
            if s[index: index + length] != word:
                return False
            index += length
            if len(s) == index:
                return True
        return False

# Date  : 09/11/2021
# First attempt

class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        prefix = ''
        for word in words:
            prefix += word
            if prefix == s:
                return True
        return False    
