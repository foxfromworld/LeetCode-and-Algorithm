# Source : https://leetcode.com/problems/same-tree/
# Author : foxfromworld
# Date  : 12/04/2021
# First attempt 

class Solution:
  def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    if p == q == None: return True
    if p and q and p.val == q.val:
      return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    else:
      return False
