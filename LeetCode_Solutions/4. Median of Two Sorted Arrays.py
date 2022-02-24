# Source : https://leetcode.com/problems/median-of-two-sorted-arrays/
# Author : foxfromworld
# Date  : 24/04/2022
# Second attempt

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        n1, n2 = len(nums1), len(nums2)            
        leftPartLen = (n1 + n2 + 1) // 2
        n1_left, n1_right = 0, n1
        while n1_left <= n1_right: # binary search
            n1_idx = (n1_left + n1_right) // 2
            n2_idx = leftPartLen - n1_idx
            
            # For min and max comparison
            n1LeftMax = float('-inf') if n1_idx == 0 else nums1[n1_idx - 1]
            n1RightMin = float('inf') if n1_idx == n1 else nums1[n1_idx]
            n2LeftMax = float('-inf') if n2_idx == 0 else nums2[n2_idx - 1]
            n2RightMin = float('inf') if n2_idx == n2 else nums2[n2_idx]
            
            if n1LeftMax > n2RightMin:
                n1_right = n1_idx - 1
            elif n2LeftMax > n1RightMin:
                n1_left = n1_idx + 1
            else:
                if (n1 + n2) % 2 == 0:
                    return (max(n1LeftMax, n2LeftMax) + min(n1RightMin, n2RightMin)) / 2
                else:
                    return max(n1LeftMax, n2LeftMax)

# Date  : 11/10/2021
# First attempt

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        length = len(nums1)
        index = length // 2
        if length % 2 == 0:
            return (nums1[index-1] + nums1[index])/2
        else:
            return nums1[index]
