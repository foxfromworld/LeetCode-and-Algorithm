# Source : https://leetcode.com/problems/find-lucky-integer-in-an-array/
# Author : foxfromworld
# Date  : 28/11/2021
# First attempt

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cnt = Counter(arr)
        max_ = -1
        for key in cnt:
            if cnt[key] == key:
                max_ = max(key, max_)
        return max_
