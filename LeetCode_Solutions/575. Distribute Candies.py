# Source : https://leetcode.com/problems/distribute-candies/
# Author : foxfromworld
# Date  : 06/02/2022
# Third attempt

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(set(candyType)), len(candyType) // 2)

# Date  : 06/02/2022
# Second attempt

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        ret = len(set(candyType))
        return ret if ret <= len(candyType)/2 else len(candyType) // 2
      
# Date  : 06/02/2022
# First attempt

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        ret = 0
        n = len(candyType) / 2
        c = set()
        for candy in candyType:
            if candy not in c:
                c.add(candy)
                ret += 1
            if ret == n:
                return ret
        return ret
