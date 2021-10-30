# Source : https://leetcode.com/problems/valid-word-abbreviation/
# Author : foxfromworld
# Date  : 30/10/2021
# First attempt

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0
        while i < len(word) and j < len(abbr):
            if abbr[j].isalpha():
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
            else:
                if abbr[j] == '0':
                    return False
                temp = ''
                while j < len(abbr) and abbr[j].isdigit():
                    temp += abbr[j]
                    j += 1
                i += int(temp)
        return i == len(word) and j == len(abbr)
            
