# Source : https://leetcode.com/problems/angle-between-hands-of-a-clock/
# Author : foxfromworld
# Date  : 10/11/2021
# First attempt

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        angle_hour, angle_min = 30, 6        
        diff = abs(minutes * angle_min - (hour +  minutes/60 ) * angle_hour)
        return min(diff, 360 - diff)
