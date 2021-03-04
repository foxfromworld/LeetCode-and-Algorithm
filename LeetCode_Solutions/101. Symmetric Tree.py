# Source : https://leetcode.com/problems/symmetric-tree/
# Author : foxfromworld
# Date  : 04/03/2021
# First attempt 

class Solution:
  def sym(self, left, right):
    if left == right == None: 
        return True
    if left and right and left.val == right.val: 
      return self.sym(left.left, right.right) and self.sym(left.right, right.left)
    else: 
        return False
  def isSymmetric(self, root: TreeNode) -> bool:
    if root == None: 
        return True
    return self.sym(root.left, root.right)
