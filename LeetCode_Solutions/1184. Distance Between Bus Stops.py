# Source : https://leetcode.com/problems/distance-between-bus-stops/
# Author : foxfromworld
# Date  : 07/12/2021
# First attempt

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        target, total = 0, 0
        if start > destination:
            start, destination = destination, start
        for i, d in enumerate(distance):
            if start <= i < destination:
                target += d
            total += d
        return min(total - target, target)
