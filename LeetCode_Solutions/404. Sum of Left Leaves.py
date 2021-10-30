# Source : https://leetcode.com/problems/sign-of-the-product-of-an-array/
# Author : foxfromworld
# Date  : 30/10/2021
# First attempt

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def help(node, isLeft):
            if not node.left and not node.right: return node.val if isLeft else 0
            ret = 0
            if node.left:
                ret += help(node.left, True)
            if node.right:
                ret += help(node.right, False)
            return ret
        return help(root, False)
