# Source : https://leetcode.com/problems/closest-binary-search-tree-value/
# Author : foxfromworld
# Date  : 06/01/2021
# First attempt 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
  def closestValue(self, root: TreeNode, target: float) -> int:
    closest = root.val
    while root:
      closest = root.val if abs(closest - target) > abs(root.val - target) else closest
      root = root.right if target > root.val else root.left
    return closest
