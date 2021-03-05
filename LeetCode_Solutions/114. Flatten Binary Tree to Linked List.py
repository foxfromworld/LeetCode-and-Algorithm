# Source : https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
# Author : foxfromworld
# Date  : 05/03/2021
# First attempt # Recursive

class Solution:
  def doFlatten(self, node):
    if not node: return None
    if not node.left and not node.right: return node
    leftend = self.doFlatten(node.left)
    rightend = self.doFlatten(node.right) 
    if leftend:
      leftend.right = node.right
      node.right = node.left
      node.left = None
    return rightend if rightend else leftend
  def flatten(self, root: TreeNode) -> None:
    """
    Do not return anything, modify root in-place instead.
    """
    self.doFlatten(root)
