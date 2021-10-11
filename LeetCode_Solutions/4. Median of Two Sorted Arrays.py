# Source : https://leetcode.com/problems/median-of-two-sorted-arrays/
# Author : foxfromworld
# Date  : 11/10/2021
# Second attempt



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
