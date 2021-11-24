# Source : https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/
# Author : foxfromworld
# Date   : 24/11/2021
# First attempt

class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        cnt = Counter([chip % 2 for chip in chips])
        return min(cnt[0], cnt[1])
