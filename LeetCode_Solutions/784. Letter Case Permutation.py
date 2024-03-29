# Source : https://leetcode.com/problems/letter-case-permutation/
# Author : foxfromworld
# Date  : 11/02/2022
# Second attempt

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ret = [[]]
        for ch in s:
            length = len(ret)
            if ch.isalpha():
                for i in range(length):
                    ret.append(ret[i][:])
                    ret[i].append(ch.lower())
                    ret[length + i].append(ch.upper())
            else:
                for i in range(length):
                    ret[i].append(ch)
        return map("".join, ret)

# Date  : 11/02/2022
# First attempt

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def recursion(st):
            if st == len(s):    
                ret.append("".join(arr))
                return
            if s[st].isalpha():
                arr[st] = arr[st].lower()
                recursion(st + 1)
                arr[st] = arr[st].upper()
                recursion(st + 1)
            else:
                recursion(st + 1)
        arr = list(s)
        ret = []
        recursion(0)
        return ret
