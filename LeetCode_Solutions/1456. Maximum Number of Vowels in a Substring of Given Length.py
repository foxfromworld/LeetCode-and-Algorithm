# Source : https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
# Author : foxfromworld
# Date  : 22/12/2021
# Second attempt

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        temp = 0
        for ch in s[:k]:
            if ch in 'aeiou':
                temp += 1
        ret = temp
        for i in range(k, len(s)):
            if s[i] in 'aeiou':
                temp += 1
            if s[i - k] in 'aeiou':
                temp -= 1
            ret = temp if ret < temp else ret
        return ret

# Date  : 22/12/2021
# First attempt

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ret = temp = 0
        for i, ch in enumerate(s):
            if ch in 'aeiou':
                temp += 1
            if i >= k and s[i - k] in 'aeiou':
                temp -= 1
            ret = max(ret, temp)
        return ret
