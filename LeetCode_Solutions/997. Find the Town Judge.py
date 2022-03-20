# Source : https://leetcode.com/problems/find-the-town-judge/
# Author : foxfromworld
# Date   : 19/03/2021
# First attempt

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust: return 1 if n == 1 else -1
        dict_ = defaultdict(int)
        for _, (ai, bi) in enumerate(trust):
            dict_[bi] += 1
            dict_[ai] -= 1
        for key in dict_:
            if dict_[key] == n - 1:
                return key
        return -1
