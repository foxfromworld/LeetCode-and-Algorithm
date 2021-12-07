# Source : https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/
# Author : foxfromworld
# Date  : 07/12/2021
# First attempt

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        counter = defaultdict(list)
        ret = []
        for i in arr:
            freq = bin(i)[2:].count('1')
            if freq in counter:
                counter[freq].append(i)
            else:
                counter[freq] = [i]
        keys = sorted(counter.keys())
        for key in keys:
            ret += sorted(counter[key])
        return ret
