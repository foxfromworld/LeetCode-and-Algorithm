# Source : https://leetcode.com/problems/keyboard-row/
# Author : foxfromworld
# Date  : 24/10/2021
# Second attempt 

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keys = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        ret = words[:]
        for word in words:
            w = word.lower()
            i= 0
            if w[0] in keys[1]: i= 1
            elif w[0] in keys[2]: i= 2
            j = 1
            while j < len(w):
                if not w[j] in keys[i]:
                    ret.remove(word)
                    break
                j += 1
        return ret

# Date  : 24/10/2021
# First attempt 

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        l1, l2, l3 = set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")
        ret = []
        for word in words:
            w = set(word.lower())
            if  w & l1 == w or w & l2 == w or w & l3 == w:
                ret.append(word)
        return ret
