# Source : https://leetcode.com/problems/combination-sum-ii/
# Author : foxfromworld
# Date   : 10/02/2022
# First attempt

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(st, curr, remainder):
            if remainder == 0:
                ret.append(curr[:])
                return
            for j in range(st, len(candidates)):
                if j > st and candidates[j] == candidates[j - 1]:
                    continue
                if remainder - candidates[j] < 0:
                    break
                curr.append(candidates[j])
                backtrack(j + 1, curr, remainder - candidates[j])
                curr.pop()
        ret = []
        candidates.sort()
        backtrack(0, [], target)
        return ret            
