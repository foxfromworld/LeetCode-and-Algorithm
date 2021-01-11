# Source : https://leetcode.com/problems/insert-into-a-binary-search-tree/
# Author : foxfromworld
# Date  : 11/01/2020
# Second attempt (recursive)

class Solution:
  def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
    if not root:
      return TreeNode(val)
    if val > root.val: # Recusively find the place to insert the node. Bigger -> right; Smaller -> left.
      root.right = self.insertIntoBST(root.right, val) 
    else:
      root.left = self.insertIntoBST(root.left, val)
    return root

# Date  : 11/01/2021
# First attempt (iterative)

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right  

class Solution:
  def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
    new = TreeNode(val)
    current = root
    while current: # Keep finding the place to insert the node. Bigger -> right; Smaller -> left.
      if val > current.val:
        if current.right == None:
          current.right = new
          return root
        else:
          current = current.right
      else:
        if current.left == None:
          current.left = new
          return root
        else:
          current = current.left
    return new
