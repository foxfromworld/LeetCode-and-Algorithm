# Source : https://leetcode.com/problems/relative-ranks/
# Author : foxfromworld
# Date  : 27/11/2021
# First attempt

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        new = sorted(score, reverse = True)
        place = ['Gold Medal', 'Silver Medal', 'Bronze Medal']
        digit = 4
        for _ in range(len(score) - len(place)):
            place.append(str(digit))
            digit += 1
        dictionary = {}
        for digi, place in zip(new, place) :
            dictionary[digi] = place
        res = []
        for s in score:
            res.append(dictionary[s])
        return res
