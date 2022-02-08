# Source : https://leetcode.com/problems/combination-sum/
# Author : foxfromworld
# Date  : 08/02/2022
# First attempt

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        def backtrack(combi, remainder, st):
            if remainder == 0:
                #ret.append(combi) # incorrect
                ret.append(combi[:]) # shallow copy
                #ret.append(combi.copy()) # shallow copy
                #ret.append(list(combi)) # shallow copy
                #ret.append(copy.deepcopy(combi)) # deep copy            
                return
            elif remainder < 0:
                return
            for i in range(st, len(candidates)):
                combi.append(candidates[i])
                backtrack(combi, remainder - candidates[i], i)
                combi.pop()
        backtrack([], target, 0)
        return ret
