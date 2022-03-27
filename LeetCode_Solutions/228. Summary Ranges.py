# Source : https://leetcode.com/problems/summary-ranges/
# Author : foxfromworld
# Date   : 27/03/2022
# Second attempt

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return []
        s = 0
        ret = []
        for i in range(len(nums) - 1):
            if nums[i] + 1 != nums[i+1]:
                if i != s:
                    ret.append(str(nums[s])+"->"+str(nums[i]))
                else:
                    ret.append(str(nums[s]))
                s = i + 1
        if s == len(nums)-1:
            ret.append(str(nums[s]))
        else:
            ret.append(str(nums[s])+"->"+str(nums[-1]))
        return ret

# Date   : 27/03/2022
# First attempt

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        ret = []
        i = 0
        for j in range(n):
            if j < i: continue
            while j + 1 < n and nums[j] + 1 == nums[j + 1]:
                j += 1
            if i == j:
                ret.append(str(nums[i]))
            else:
                ret.append(str(nums[i]) + "->" + str(nums[j]))
            i = j + 1
        return ret
