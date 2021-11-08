# Source : https://leetcode.com/problems/pour-water/
# Author : foxfromworld
# Date  : 08/11/2021
# First attempt

class Solution:
    def pourWater(self, heights: List[int], volume: int, k: int) -> List[int]:
        i = k        
        for _ in range(volume):
            while i > 0 and heights[i] >= heights[i-1]:
                i -= 1
            while i < len(heights) - 1 and heights[i] >= heights[i+1]:
                i += 1
            while i > k and heights[i] == heights[i-1]:
                i -= 1
            heights[i] += 1
        return heights 
