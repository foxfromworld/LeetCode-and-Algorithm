# Source : https://leetcode.com/problems/letter-case-permutation/
# Author : foxfromworld
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
