# Source : https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/
# Author : foxfromworld
# Date  : 12/12/2021
# First attempt

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i in range(len(prices)-1):
            j = i + 1
            while j < len(prices):
                if prices[j] <= prices[i]:
                    prices[i] -= prices[j]
                    break
                j += 1
        return prices
