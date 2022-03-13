# Source : https://leetcode.com/problems/next-permutation/
# Author : foxfromworld
# Date   : 13/03/2022
# First attempt

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1 5 8 4 7 6 5 3 1
        #                 ij
        i = j = len(nums) - 1
        while i > 0 and nums[i-1] >= nums[i]: # find the first decreasing element
            i -= 1
        # 1 5 8 4 7 6 5 3 1
        #         i       j    
        if i == 0: 
            nums.reverse()
            return
        while nums[j] <= nums[i-1]: #find the first element larger than nums[i]
            j -= 1
        # 1 5 8 4 7 6 5 3 1
        #      i-1    j    
        nums[i-1], nums[j] = nums[j], nums[i-1]
        # 1 5 8 5 7 6 4 3 1
        #         s       e            
        s, e = i, len(nums) - 1
        while s < e:
            nums[s], nums[e] = nums[e], nums[s]
            s += 1
            e -= 1
