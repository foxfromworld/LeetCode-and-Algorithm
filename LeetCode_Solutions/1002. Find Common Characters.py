# Source : https://leetcode.com/problems/find-common-characters/
# Author : foxfromworld
# Date  : 04/11/2021
# Second attempt

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        num = Counter(words[0])
        ans = []
        for i in range(1, len(words)):
            num &= Counter(words[i])
        return list(num.elements())

# Date  : 04/11/2021
# First attempt

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        num = Counter(words[0])
        ans = []
        for i in range(1, len(words)):
            num &= Counter(words[i])
        for ch in num:
            for _ in range(num[ch]):
                ans.append(ch)    
        return ans
