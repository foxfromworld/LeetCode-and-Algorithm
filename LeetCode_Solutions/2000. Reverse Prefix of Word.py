# Source : https://leetcode.com/problems/reverse-prefix-of-word/
# Author : foxfromworld
# Date  : 29/09/2021
# First attempt 

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i, char in enumerate(word):
            if char == ch:
                return word[:i+1][::-1] + word[i+1:]
        return word
