# Source : https://leetcode.com/problems/invert-binary-tree/
# Author : foxfromworld
# Date  : 18/01/2021
# First attempt 

#     4
#   /   \
#  2     7
# / \   / \
#1   3 6   9
# ==>
#     4
#   /   \
#  7     2
# / \   / \
#6   9 3   1
# ==>
#     4
#   /   \
#  7     2
# / \   / \
#9   6 3   1


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
  def invertTree(self, root: TreeNode) -> TreeNode:
    if root:
      root.right, root.left = root.left, root.right
      self.invertTree(root.right)          
      self.invertTree(root.left)      
    return root
    
    
