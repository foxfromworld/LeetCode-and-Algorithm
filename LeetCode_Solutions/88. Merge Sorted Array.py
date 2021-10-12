# Source : https://leetcode.com/problems/merge-sorted-array/
# Author : foxfromworld
# Date  : 12/10/2021
# Second attempt

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2= m-1, n-1
        for p in range(m+n-1, -1, -1):
            if p2 < 0:
                break
            if p1 > -1 and nums2[p2] < nums1[p1]:
                nums1[p] = nums1[p1] 
                p1 -= 1
            else: 
                nums1[p] = nums2[p2]
                p2 -= 1                

# Date  : 12/10/2021
# First attempt

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2[:]
        nums1.sort()
