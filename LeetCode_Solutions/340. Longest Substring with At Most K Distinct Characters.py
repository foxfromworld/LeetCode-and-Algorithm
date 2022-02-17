# Source : https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
# Author : foxfromworld
# Date  : 17/02/2022
# First attempt

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        dict_ = defaultdict(int)
        st = 0
        for ed, ch in enumerate(s):
            dict_[ch] += 1
            if len(dict_) > k:
                dict_[s[st]] -= 1
                if dict_[s[st]] == 0:
                    del dict_[s[st]]
                st += 1
        return ed - st + 1
