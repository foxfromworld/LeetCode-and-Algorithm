# Source : https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/
# Author : foxfromworld
# Date  : 17/11/2021
# Second attempt

class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        max_ = 0
        cnt = 0
        for rect in rectangles:
            min_ = min(rect)
            if max_ < min_:
                max_, cnt = min_, 1
            elif max_ == min_:
                cnt += 1
        return cnt

# Date  : 17/11/2021
# First attempt

class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        num = []
        max_ = 0
        for rect in rectangles:
            min_ = min(rect)
            num.append(min_)
            max_ = max(max_, min_)
        return num.count(max_)
