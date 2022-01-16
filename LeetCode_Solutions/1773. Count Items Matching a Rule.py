# Source : https://leetcode.com/problems/count-items-matching-a-rule/
# Author : foxfromworld
# Date  : 16/01/2022
# First attempt

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if ruleKey == "type":
            idx = 0
        elif ruleKey == "color":
            idx = 1
        else:
            idx = 2
        ret = 0
        for item in items:
            if item[idx] == ruleValue:
                ret += 1
        return ret                
