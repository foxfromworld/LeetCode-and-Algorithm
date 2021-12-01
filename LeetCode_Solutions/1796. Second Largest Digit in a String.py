# Source : https://leetcode.com/problems/second-largest-digit-in-a-string/
# Author : foxfromworld
# Date  : 01/12/2021
# First attempt

class Solution:
    def secondHighest(self, s: str) -> int:
        ret = []
        heapq.heapify(ret)
        for ch in s:
            if ch.isdigit() and not int(ch) in ret:
                heapq.heappush(ret, int(ch))
        ret = heapq.nlargest(2, ret)
        return  ret[1] if len(set(ret)) > 1 else -1
