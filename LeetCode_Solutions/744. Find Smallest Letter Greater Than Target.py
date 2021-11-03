# Source : https://leetcode.com/problems/find-smallest-letter-greater-than-target/
# Author : foxfromworld
# Date  : 03/11/2021
# First attempt

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for letter in letters:
            if letter > target:
                return letter
        return letters[0]
