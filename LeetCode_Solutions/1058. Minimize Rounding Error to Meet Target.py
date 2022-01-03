# Source : https://leetcode.com/problems/minimize-rounding-error-to-meet-target/
# Author : foxfromworld
# Date  : 03/01/2022
# First attempt

class Solution:
    def minimizeError(self, prices: List[str], target: int) -> str:
        low, high, diffs = 0, 0, []
        for price in prices:
            price = float(price)
            ceil = math.ceil(price)
            floor = math.floor(price)
            low += floor
            high += ceil
            if floor != ceil:
                diffs.append([ceil - price, price - floor])
        if target < low or high < target: return "-1"
        diffs.sort()
        gap = target - low
        return '{:.3f}'.format(sum([diff[0] for diff in diffs[:gap]]) + sum([diff[1] for diff in diffs[gap:]]))
