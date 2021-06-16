# Source : https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Author : foxfromworld
# Date  : 16/06/2021
# F attempt

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits: return []
        letters = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno',
                   '7':'pqrs', '8':'tuv', '9':'wxyz'}
        def backtrack(index, path):
          if len(path) == len(digits):
            combinations.append(''.join(path))
            return
          possible_letters = letters[digits[index]]
          for letter in possible_letters:
            path.append(letter)
            backtrack(index + 1, path)
            path.pop()
        combinations = []
        backtrack(0, [])
        return combinations
