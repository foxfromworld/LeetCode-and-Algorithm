# Source : https://leetcode.com/problems/majority-element-ii/
# Author : foxfromworld
# Date  : 22/02/2022
# First attempt

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt1, cnt2, major1, major2 = 0, 0, None, None
        dict_ = defaultdict(int)
        ret = []
        for num in nums:
            if major1 == num:
                cnt1 += 1
            elif major2 == num:
                cnt2 += 1
            elif cnt1 == 0:
                major1 = num
                cnt1 = 1
            elif cnt2 == 0:
                major2 = num
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1
            dict_[num] += 1
        n = len(nums) // 3
        if dict_[major1] > n:
            ret.append(major1)
        if dict_[major2] > n:
            ret.append(major2) 
        return ret
