# Source : https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# Author : foxfromworld
# Date  : 15/10/2021
# Second attempt

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(left, right):
            if left > right: return None
            pivot = (left + right) >> 1
            return TreeNode(nums[pivot], helper(left, pivot - 1), helper(pivot + 1, right))
        return helper(0, len(nums) - 1)

# Date  : 15/10/2021
# First attempt

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(left, right):
            if left > right: return None
            
            pivot = (left + right) // 2
            root = TreeNode(nums[pivot])
            root.left = helper(left, pivot - 1)
            root.right = helper(pivot + 1, right)
            return root
        
        root = helper(0, len(nums) - 1)
        return root
